from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.shortcuts import redirect

def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def about(request):
    context = {}
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def redirect_view(request):
    response = redirect('/contact/')
    return response