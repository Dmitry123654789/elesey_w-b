from django.shortcuts import render
from django.utils.translation import gettext_lazy as _


def all_pages(request, name_page):
    return render(request, f"home/{name_page}.html")


def index(request):
    marketing_pages = {
        "Outdoor_advertising": _("Наружная реклама"),
        "Event_marketing": _("Событийный маркетинг"),
        "PR": _("PR и СМИ"),
        "Sales_Promotion": _("Стимулирование сбыта"),
        "SEO": _("SEO-оптимизация"),
        "Contextual_advertising": _("Контекстная реклама"),
        "SMM": "SMM",
        "Content_marketing": _("Контент-маркетинг"),
        "Email_marketing": _("Email маркетинг"),
        "SERM": "SERM",
    }
    return render(request, "home/index.html", {"pages": marketing_pages})
