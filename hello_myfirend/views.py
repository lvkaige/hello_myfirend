from django.shortcuts import render

from django.http import HttpResponse

from django import forms


def index(request):
    return render(request, "friends/index.html")


def hello(request):
    return render(request, "friends/hello.html")

def hello2(request):
    return render(request, "friends/hello2.html")

def hello3(request):
    return render(request, "friends/hello3.html")

def hello4(request):
    return render(request, "friends/hello4.html")


