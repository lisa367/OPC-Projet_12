from Model.base import filter_table, update
from Model.collaborateurs import collaborateurs_colonnes
from Model.contrats import contrats_colonnes
from Model.evenements import evenements_colonnes
from View.base import CRUD_MENU, affichage_menu, get_query_filters, get_object_id, get_object_data
from View.gestion import GESTION_MENU
from .base import operations_crud, modifier, quitter, afficher_table


def affichage_evenements():
	columns, conditions = get_query_filters(evenements_colonnes)
	query_result = filter_table("evenements", columns, conditions)
	print(query_result)


def support_evenements():
	# modifier(object_name, table_name, table_columns)
	id_evenement = get_object_id()
	data_evenement = get_object_data("evenement", ["support_collaborateur_id"])
	update("evenements", id_evenement, data_evenement)


def gestion_controller():
	show_menu = True
	while show_menu:
		options = {"1": "gestion-collaborateurs", "2": "gestion-contrats", "3": "affichage-evenements", "4": "support-evenements", "5": "afficher-table", "6": "quitter"}
		menu_choisi = affichage_menu(GESTION_MENU, options)

		if menu_choisi == "gestion-collaborateurs":
			operations_crud(object_name="collaborateur", table_name="collaborateurs", table_columns=collaborateurs_colonnes)
		elif menu_choisi == "gestion-contrats":
			operations_crud(object_name="contrat", table_name="contrats", table_columns=contrats_colonnes)
		elif menu_choisi == "affichage-evenements":
			affichage_evenements()
		elif menu_choisi == "support-evenements":
			support_evenements()
		elif menu_choisi == "afficher-table":
			afficher_table()
		elif menu_choisi == "quitter":
			show_menu = False
		else :
			print("Veuillez saisir une entrée valide")
	quitter()