import os
from Model.base import new_entry, update, filter_table
from Model.contrats import contrats_colonnes
from Model.clients import clients_colonnes
from Model.evenements import evenements_colonnes
from View.base import affichage_menu, get_object_id, get_query_filters, add_or_modify, get_object_data
from View.commercial import COMMERCIAL_MENU
from .base import ajouter, modifier, quitter, operations_crud

def commercial_controller():
	show_menu = True
	while show_menu:
		options = {"1": "clients", "2": "modification-contrats", "3": "affichage-contrats", "4": "evenements", "5": "afficher-table", "6": "quitter"}
		menu_choisi = affichage_menu(COMMERCIAL_MENU, options)

		if menu_choisi == "clients":
			USER_ID = os.getenv("USER_ID")
			operations_crud(object_name="client", table_name="clients", table_columns=clients_colonnes, default_values=[("collaborateur_id", USER_ID)])

		elif menu_choisi == "modification-contrats":
			modifier("contrat", "contrats", contrats_colonnes)

		elif menu_choisi == "affichage-contrats":
			columns, conditions = get_query_filters(contrats_colonnes)
			query_result = filter_table("contrats", columns, conditions)
			print(query_result)

		elif menu_choisi == "evenements":
			ajouter("evenement", "evenements", evenements_colonnes)
			""" action = add_or_modify("evenement")
			if action == "ajouter":
				ajouter("evenement", "evenements", evenements_colonnes)
			elif action == "modifier":
				modifier("evenement", "evenements", evenements_colonnes) """

		elif menu_choisi == "afficher-table":
				pass

		elif menu_choisi == "quitter":
			show_menu = False

		else :
			print("Veuillez saisir une entrée valide")

	quitter()


""" 
def commercial_controller():
	options = {"1": "clients", "2": "gestion-contrats", "3": "affichage-contrats", "4": "evenements"}
	menu_choisi = affichage_menu(COMMERCIAL_MENU, options)
	if menu_choisi == "clients":
		id_utilisateur = get_object_id("collaborateur")
		data_client = get_object_data("client", clients_colonnes)
		new_entry("clients", id_utilisateur)
	elif menu_choisi == "gestion-contrats":
		pass
	elif menu_choisi == "affichage-contrats":
		columns, conditions = get_query_filters(contrats_colonnes)
		query_result = filter_table("contrats", columns, conditions)
		print(query_result)
	elif menu_choisi == "evenements":
		action = add_or_modify("evenement")
		if action == "ajouter":
			data_evenement = get_object_data("evenement", evenements_colonnes)
			new_entry("evenements", evenements_colonnes, data_evenement)
		elif action == "modifier":
			id_evenement = get_object_id("evenement")
			data_evenement = get_object_data("evenement", evenements_colonnes)
			update("evenements", id_evenement ,data_evenement)
	else :
		return 0
"""