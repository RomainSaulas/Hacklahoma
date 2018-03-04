from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404


from .models import Technologies, Waste, Transaction, Company, Project, WastePricing

def home(request):
    return render(request, 'home.html')
	
def about(request):
    return render(request, 'about.html')
	
def legalInfo(request):
    return render(request, 'legalInfo.html')
	
def signing(request):
    return render(request, 'signing.html')

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
    return render(request, 'myAccount.html', {'user': user})
	
def trading(request):		
	return render(request, 'trading.html', {'trans': Transaction.objects.all(), 'company': Company.objects.all()})
	
def wastes(request):
    try:
        wastes = Waste.objects.all()
    except Waste.DoesNotExist:
        raise Http404('No Wastes Available Now')
    return render(request, 'wastes.html', {'wastes': wastes})	
	
def projects(request):
	# for proj in Project.objects.all():
		# try:
			# offers = WastePricing.objects.get(name = proj.wasteName)
			# min = 0
			# for offer in offers:
				# if offer.price > min:
					# min = offer.price
			# proj.bestCompanyId = WastePricing.objects.get(price = min).companyId
		# except Company.DoesNotExist :
			# raise Http404('No specific company associated to this type of waste')
		# try:
			# wId = Waste.object.get(name = proj.wasteName).id
			# tech = Technologies.object.get(companyId = proj.bestCompanyId)
			# tech = tech.get(wasteId = wId)
			# proj.bestTechnologyDesc = tech.description
		# except Technologies.DoesNotExist :
			# raise Http404('No specific technology associated to this type of waste')
		# proj.save()
	return render(request, 'projects.html', {'projects': Project.objects.all()})