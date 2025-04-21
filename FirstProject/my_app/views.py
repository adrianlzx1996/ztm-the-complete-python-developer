from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hellow world")

def about(request):
    return HttpResponse("About Me")

def hello(request, first_name):
    return HttpResponse(f"Hello {first_name}")