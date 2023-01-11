from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path


def index(request):
    return HttpResponse("Top page")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path("", index),
]
