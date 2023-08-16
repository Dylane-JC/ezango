from django.urls import path
from . import views

app_name = "ezangofilemanager"

urlpatterns =[
path("", views.connexion, name="connexion"),
path("demande", views.demande, name="demande"),
path("consultation", views.consultation, name="consultation")
]