from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("hello/", views.hello),
    path("hello/hello2/", views.hello2),
    path("hello/hello2/hello3/", views.hello3),
    path("hello/hello2/hello3/hello4/", views.hello4),
]
