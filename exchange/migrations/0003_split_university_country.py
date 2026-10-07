import re

from django.db import migrations, models

PAREN = re.compile(r"^(?P<name>.+?)\s*\((?P<country>[^()]+)\)\s*$")
DASH = re.compile(r"^(?P<name>.+?)\s+[-–—]\s+(?P<country>[^-–—]+)$")
COMMA = re.compile(r"^(?P<name>.+),\s*(?P<country>[^,]+)$")  # остання кома


def split_value(value):
    value = value.strip()
    for pattern in (PAREN, DASH, COMMA):
        m = pattern.match(value)
        if m:
            return m.group("name").strip(), m.group("country").strip()
    raise ValueError(f"Не вдалося розділити університет і країну: {value!r}")


def forwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    for p in Program.objects.all():
        p.university, p.country = split_value(p.university)
        p.save(update_fields=["university", "country"])


def backwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    for p in Program.objects.all():
        if p.country:
            p.university = f"{p.university}, {p.country}"
            p.save(update_fields=["university"])


class Migration(migrations.Migration):
    dependencies = [("exchange", "0002_seed_programs")]

    operations = [
        migrations.AddField(
            model_name="exchangeprogram",
            name="country",
            field=models.CharField(blank=True, default="", max_length=100, verbose_name="країна"),
        ),
        migrations.RunPython(forwards, backwards),
    ]
