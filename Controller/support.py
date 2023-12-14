from Model.base import new_entry, filter_table, update, get_entry, get_all
from Model.evenements import evenements_colonnes
from View.base import affichage_menu, get_object_id, get_query_filters, get_object_data, add_or_modify
from View.support import SUPPORT_MENU
from .base import ajouter, modifier, quitter

def support_controller():
	show_menu = True
	while show_menu:
		options = {"1": "affichage-evenements", "2": "gestion-evenements", "3": "afficher-table", "4": "quitter"}
		menu_choisi = affichage_menu(SUPPORT_MENU, options)

		if menu_choisi == "affichage-evenements":
			columns, conditions = get_query_filters(evenements_colonnes)
			query_result = filter_table("evenements", columns, conditions)
			print(query_result)

		elif menu_choisi == "gestion-evenements":
			id_evenement = get_object_id()
			data_evenement = get_object_data("evenement", evenements_colonnes)
			update("evenements", id_evenement, data_evenement)

		elif menu_choisi == "afficher-table":
				pass
		elif menu_choisi == "quitter":
				show_menu = False
	quitter()