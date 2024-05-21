from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is Course Page...")


def about(request):
    return HttpResponse("This is About Page...")
