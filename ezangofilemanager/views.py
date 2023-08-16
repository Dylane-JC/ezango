from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def connexion(request):
    return render(request, 'ezangofilemanager/login.html')

def demande(request):
    return render(request ,'ezangofilemanager/demandedit.html')

def consultation(request):
    return render(request, 'ezangofilemanager/consultation.html')