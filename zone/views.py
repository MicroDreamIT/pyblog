from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'zone/index.html')


def create(request):
    return render(request, 'zone/create.html')
