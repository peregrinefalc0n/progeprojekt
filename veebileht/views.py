from django.shortcuts import render
from django.http import HttpResponse
from veebileht.translate import execute
from veebileht.models import Event
# Create your views here.

#req - resp 
#view function is a function that takes a request and returns a response
#its a request handler

def returnwebpage(request):
    return render(request, 'index.html', {'events': execute()})