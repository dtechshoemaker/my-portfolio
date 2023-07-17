from django.shortcuts import path


urlpatterns = [
    path("", "views.home", name="home"),
]