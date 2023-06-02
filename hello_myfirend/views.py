from django.shortcuts import render

from django.http import HttpResponse

from django import forms


def index(request):
    return render(request, "friends/test.html")


def hello(request):
    return render(request, "friends/hello.html")


