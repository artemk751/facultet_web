from django.contrib import admin

from .models import ExchangeProgram


@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ("university", "country", "languages", "seats", "deadline", "status")
    list_filter = ("country",)
    search_fields = ("university", "country")

    @admin.display(description="статус прийому", boolean=True)
    def status(self, obj):
        return obj.is_open
