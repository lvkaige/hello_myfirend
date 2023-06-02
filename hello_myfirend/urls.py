from django.urls import path, include

from . import views

app_name = "hello_myfriend"

urlpatterns = [
    path("", views.index, name="index"),
]
