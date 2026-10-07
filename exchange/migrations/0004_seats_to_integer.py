import re

from django.db import migrations, models


def forwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    for p in Program.objects.all():
        m = re.search(r"\d+", p.seats_text)
        if not m:
            raise ValueError(f"У значенні кількості місць немає числа: {p.seats_text!r}")
        p.seats = int(m.group())
        p.save(update_fields=["seats"])


def backwards(apps, schema_editor):
    Program = apps.get_model("exchange", "ExchangeProgram")
    for p in Program.objects.all():
        p.seats_text = str(p.seats)
        p.save(update_fields=["seats_text"])


class Migration(migrations.Migration):
    dependencies = [("exchange", "0003_split_university_country")]

    operations = [
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.CharField(blank=True, default="", max_length=50, verbose_name="кількість місць"),
        ),
        migrations.RenameField("exchangeprogram", "seats", "seats_text"),
        migrations.AddField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveIntegerField(null=True, verbose_name="кількість місць"),
        ),
        migrations.RunPython(forwards, backwards),
        migrations.RemoveField("exchangeprogram", "seats_text"),
        migrations.AlterField(
            model_name="exchangeprogram",
            name="seats",
            field=models.PositiveIntegerField(verbose_name="кількість місць"),
        ),
    ]
