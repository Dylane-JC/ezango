from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def connexion(request):
    context = {}

    #On recupere les informations du formulaire tout en verifiant la methode de transmission des data
    if request.method == 'POST':
        #On initialise les variables username et password
        username = request.POST['username']
        password = request.POST['password']

        #On authentifie l'utilisateur
        user = authenticate(username=username, password=password)
        #Si l'utilisateur est autorisé, il est redirigé vers la page d'accueil
        if user is not None:
            login(request, user)
            return redirect('ezangofilemanager:demande', {'msg':''})
        else:
            return render(request, 'ezangofilemanager/login.html', {'msg':'Il semble que votre identifiant ou votre code de sécurité est incorrect'})
    return render(request, 'ezangofilemanager/login.html')

def deconnexion(request):
    logout(request)
    return redirect('ezangofilemanager:connexion')

def demande(request):
    return render(request ,'ezangofilemanager/demandedit.html')

def consultation(request):
    return render(request, 'ezangofilemanager/consultation.html')


