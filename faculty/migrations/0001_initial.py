import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="назва")),
                ("head", models.CharField(max_length=150, verbose_name="завідувач кафедри")),
            ],
            options={"verbose_name": "кафедра", "verbose_name_plural": "кафедри", "ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="назва факультету")),
                ("description", models.TextField(verbose_name="опис факультету")),
                ("info", models.TextField(blank=True, verbose_name="основна інформація")),
                ("contacts", models.TextField(blank=True, verbose_name="контакти")),
            ],
            options={"verbose_name": "головна сторінка", "verbose_name_plural": "головна сторінка"},
        ),
        migrations.CreateModel(
            name="Program",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=200, verbose_name="назва")),
                ("code", models.CharField(max_length=20, verbose_name="код")),
                ("description", models.TextField(verbose_name="опис")),
                ("coordinator_name", models.CharField(max_length=150, verbose_name="імʼя координатора набору")),
                ("coordinator_contact", models.CharField(max_length=200, verbose_name="контакт координатора набору")),
                ("subjects", models.TextField(blank=True, help_text="Кожна дисципліна з нового рядка.", verbose_name="список дисциплін")),
                ("department", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="programs", to="faculty.department", verbose_name="випускова кафедра")),
            ],
            options={"verbose_name": "спеціальність", "verbose_name_plural": "спеціальності", "ordering": ["code", "name"]},
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=150, verbose_name="імʼя")),
                ("position", models.CharField(max_length=150, verbose_name="посада")),
                ("degree", models.CharField(blank=True, max_length=150, verbose_name="науковий ступінь")),
                ("department", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="teachers", to="faculty.department", verbose_name="кафедра")),
            ],
            options={"verbose_name": "викладач", "verbose_name_plural": "викладачі", "ordering": ["name"]},
        ),
    ]
