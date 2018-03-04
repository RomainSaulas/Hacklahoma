from csv import DictReader

from django.core.management import BaseCommand

from objectivezero.models import Company, User, Waste, Transaction, Technologies, WastePricing


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
	# Show this when the user types help
	help = "Loads data from data.csv into our models"
	def handle(self, *args, **options):
		if Company.objects.exists() or User.objects.exists() or Waste.objects.exists() or Transaction.objects.exists() or Technologies.objects.exists() or WastePricing.objects.exists():
			print(ALREADY_LOADED_ERROR_MESSAGE)
			return
		print("Loading data for objectivezero website")
		for row in DictReader(open('./data.csv')):
			company = Company()
			user = User()
			waste = Waste()
			transaction = Transaction()
			technologies = Technologies()
			wastepricing = WastePricing()
			company.id = row['Cid']
			company.name = row['Cname']
			company.country = row['Country']
			company.adress = row['Cadress']
			company.contactUserId = row['Contact']
			company.sector = row['Sector']
			company.save()
			user.id = row['Userid']
			user.name = row['Uname']
			user.phone = row['Phone']
			user.adress = row['Uadress']
			user.companyId = row['CompId']
			user.status = row['Status']
			user.save()
			waste.id = row['Wid']
			waste.name = row['Wname']
			waste.estPrice = row['EPrice']
			waste.recyclingScore = row['Score']
			waste.save()
			transaction.sellingCompanyId = row['SCid']
			transaction.buyingCompanyId = row['BCid']
			transaction.wasteId = row['wid']
			transaction.cost = row['cost']
			transaction.save()
			technologies.companyId = row['Tcid']
			technologies.wasteId = row['Twid']
			technologies.isPatented = row['Patent']
			technologies.description = row['Desc']
			technologies.save()
			wastepricing.companyId = row['WCid']
			wastepricing.wasteId = row['Wwid']
			wastepricing.price = row['Price']
			wastepricing.minQuantity = row['MinQuantity']
			wastepricing.save()
        
