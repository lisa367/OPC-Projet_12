# from Model.base import new_entry, get_entry, get_all
# from Model.collaborateurs import collaborateurs_colonnes
from View.base import CRUD_MENU, affichage_menu, operations_crud
from View.gestion import GESTION_MENU

def gestion_collaborateurs():
	print("Ajouter, modifier, ou supprimer un collaborateur")
	options = {"1": "ajouter", "2": "modifier", "3": "supprimer", "4": "retour", }
	option_choisie = affichage_menu(CRUD_MENU, options)

def gestion_contrats():
	print("Ajouter, modifier, ou supprimer un contrat")
	options = {"1": "ajouter", "2": "modifier", "3": "supprimer", "4": "retour", }
	option_choisie = affichage_menu(CRUD_MENU, options)

def affichage_evenements():
	pass

def support_evenements():
	pass

def gestion_controller():
	options = {"1": "collaborateurs", "2": "contrats", "3": "affichage-evenements", "4": "support-evenements", }
	menu_choisi = affichage_menu(GESTION_MENU, options)

	if menu_choisi == "collaborateurs":
		pass
		# operations_crud(object_name="collaborateurs", table_name="collaborateurs", table_columns=collaborateurs_colonnes)
	elif menu_choisi == "contrats":
		pass
		# operations_crud(object_name, table_name, table_columns)
	elif menu_choisi == "affichage-evenements":
		pass
	elif menu_choisi == "support-evenements":
		pass
	else :
		return 0