from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Technologies
from .models import User

def home(request):
    return render(request, 'home.html')
	
def about(request):
    return render(request, 'home.html')
	
def legalInfo(request):
    return render(request, 'home.html')
	
def signing(request):
    return render(request, 'home.html')

def technologies(request):
    try:
        techs = Technologies.objects.all()
    except Technologies.DoesNotExist:
        raise Http404('No Technologies Available Now')
    return render(request, 'technologies.html', {'techs': techs})

def myAccount(request, id):
    try:
        user = User.objects.get(id = id)
    except User.DoesNotExist:
        raise Http404('User Not Found')
    return render(request, 'home.html', {'user': user})
	
def trading(request):
    return render(request, 'home.html')
	
def project(request):
    return render(request, 'home.html')