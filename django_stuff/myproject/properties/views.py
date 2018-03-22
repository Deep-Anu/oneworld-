from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
	return HttpResponse("List of properties 154 van reipen  8 perrine ave ")
