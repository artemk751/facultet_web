from django.shortcuts import render

from .models import ExchangeProgram


def exchange_list(request):
    country = request.GET.get("country", "").strip()
    programs = ExchangeProgram.objects.all()
    if country:
        programs = programs.filter(country=country)
    countries = (
        ExchangeProgram.objects.exclude(country="")
        .order_by("country")
        .values_list("country", flat=True)
        .distinct()
    )
    return render(
        request,
        "exchange/exchange_list.html",
        {"programs": programs, "countries": countries, "current_country": country},
    )
