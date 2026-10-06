from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField("університет", max_length=200)
    country = models.CharField("країна", max_length=100, blank=True, default="")
    languages = models.CharField("мови навчання", max_length=200)
    seats = models.PositiveIntegerField("кількість місць")
    deadline = models.DateField("дедлайн подачі")
    description = models.TextField("опис")

    class Meta:
        verbose_name = "програма обміну"
        verbose_name_plural = "програми обміну"
        ordering = ["deadline", "university"]

    def __str__(self):
        return f"{self.university} ({self.country})" if self.country else self.university

    @property
    def is_open(self):
        """Статус прийому обчислюється з дедлайну, а не зберігається (див. ANSWERS.md).
        Дедлайн вважається включно: у день дедлайну подати заявку ще можна."""
        return self.deadline >= timezone.localdate()
