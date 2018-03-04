from django.db import models

class Company(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	adress = models.CharField(max_length=30)
	contactUserId = models.IntegerField(null = True)
	sector = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

    

class User(models.Model):
	STATUS_CHOICES = [('C', 'Company'), ('E', 'Entrepreneur'), ('O', 'Organization')]
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	adress = models.CharField(max_length=30)
	companyId = models.IntegerField(null = True)
	status = models.CharField(choices=STATUS_CHOICES, max_length=1, blank=True)
	
	def __str__(self):
		return self.name
    

class Waste(models.Model):
	id = models.IntegerField(primary_key = True)
	name = models.CharField(max_length=100)
	estPrice = models.FloatField(max_length=15)
	recyclingScore = models.IntegerField()
	
	def __str__(self):
		return self.name
		
class Transaction(models.Model):
	sellingCompanyId = models.IntegerField()
	buyingCompanyId = models.IntegerField()
	wasteId = models.IntegerField()
	cost = models.FloatField(max_length=15)
	
class Technologies(models.Model):
	name = models.CharField(max_length=50, null=True)
	companyId = models.IntegerField()
	wasteId = models.IntegerField()
	isPatented = models.BooleanField()
	description = models.TextField()
	
class WastePricing(models.Model):
	companyId = models.IntegerField()
	wasteId = models.IntegerField()
	price = models.FloatField(max_length=15)
	minQuantity = models.FloatField(null=True)
	
class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	wasteId = models.IntegerField
	bestCompanyId = models.IntegerField()
	bestTechnologyDesc = models.TextField()