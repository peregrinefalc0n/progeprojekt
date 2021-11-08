from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#req - resp 
#view function is a function that takes a request and returns a response
#its a request handler

def returnwebpage(request):
    return render(request, 'index.html', {'name': 'Robert'})