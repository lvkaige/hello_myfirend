from django.shortcuts import render

from django.http import HttpResponse

from django import forms

def index(request):
    return render(request, "friends/index.html")

