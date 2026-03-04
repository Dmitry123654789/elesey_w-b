import django.urls

import home.views


app_name = "homepage"


urlpatterns = [
    django.urls.path("<str:name_page>/", view=home.views.all_pages, name="home"),
    django.urls.path("", view=home.views.index, name="index"),
]
