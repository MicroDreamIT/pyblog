from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ZoneCreateForm


# Create your views here.
def index(request):
    return render(request, 'frontend/zone/index.html')


def create(request):
    if request.method == 'POST':
        form = ZoneCreateForm(request.POST)
        if form.is_valid():
            return render(request.user)
            form.save()

    return render(request, 'frontend/zone/create.html', {'form': ZoneCreateForm})
