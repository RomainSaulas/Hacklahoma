import networkx as nx
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt



from django.core.management import BaseCommand

from objectivezero.models import Company, Transaction




class Command(BaseCommand):
	# Show this when the user types help
	help = "Create a vizualization"
	def handle(self, *args, **options):
		labels = dict()
		transactions = Transaction.objects.all
		cies = Company.objects.all
		G=nx.Graph()
		for cy in cies:
			labels[cy.id] = cy.name
			G.add_node(cy.id)
		for trans in transactions:
			G.add_edge(sellingCompanyId, buyingCompanyId)
		nx.draw(G)
		plt.savefig("figure.png")