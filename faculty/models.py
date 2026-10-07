from django.db import models


class Department(models.Model):
    name = models.CharField("назва", max_length=200)
    head = models.CharField("завідувач кафедри", max_length=150)

    class Meta:
        verbose_name = "кафедра"
        verbose_name_plural = "кафедри"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField("назва", max_length=200)
    code = models.CharField("код", max_length=20)
    description = models.TextField("опис")
    coordinator_name = models.CharField("імʼя координатора набору", max_length=150)
    coordinator_contact = models.CharField("контакт координатора набору", max_length=200)
    department = models.ForeignKey(
        Department,
        verbose_name="випускова кафедра",
        on_delete=models.PROTECT,
        related_name="programs",
    )
    subjects = models.TextField(
        "список дисциплін", blank=True, help_text="Кожна дисципліна з нового рядка."
    )

    class Meta:
        verbose_name = "спеціальність"
        verbose_name_plural = "спеціальності"
        ordering = ["code", "name"]

    def __str__(self):
        return f"{self.code} {self.name}"

    @property
    def subjects_list(self):
        return [s.strip() for s in self.subjects.splitlines() if s.strip()]


class Teacher(models.Model):
    name = models.CharField("імʼя", max_length=150)
    position = models.CharField("посада", max_length=150)
    degree = models.CharField("науковий ступінь", max_length=150, blank=True)
    department = models.ForeignKey(
        Department,
        verbose_name="кафедра",
        on_delete=models.CASCADE,
        related_name="teachers",
    )

    class Meta:
        verbose_name = "викладач"
        verbose_name_plural = "викладачі"
        ordering = ["name"]

    def __str__(self):
        return self.name


class HomePage(models.Model):

    title = models.CharField("назва факультету", max_length=200)
    description = models.TextField("опис факультету")
    info = models.TextField("основна інформація", blank=True)
    contacts = models.TextField("контакти", blank=True)

    class Meta:
        verbose_name = "головна сторінка"
        verbose_name_plural = "головна сторінка"

    def __str__(self):
        return self.title
