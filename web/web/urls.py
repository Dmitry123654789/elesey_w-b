from django.contrib import admin
from django.urls import path, include
import django.conf.urls.i18n

import home.urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(home.urls)),
    path("i18n/", include(django.conf.urls.i18n)),
]
