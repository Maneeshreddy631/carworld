from django.shortcuts import render
from .models import Team
# Create your views here.
def home(request) :
    teams = Team.objects.all() #Team is model name #fetches all data in team model
    data = {
        'teams' : teams,
        #pass this data in to home.html
    }
    return render(request, 'pages/home.html',data)


def about(request) :
    teams = Team.objects.all()
    data = {
        'teams' : teams,

    }
    return render(request, 'pages/about.html',data)
def services(request) :
    return render(request, 'pages/services.html')
def contact(request) :
    return render(request, 'pages/contact.html')