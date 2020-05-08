from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForms

# Create your views here.

def contact(request):
    form = ContactForms()
    return render(request,"home.html",{"form" : form})