from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("")
    return render(request, 'index.html')