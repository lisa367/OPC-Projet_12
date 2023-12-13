import os
import sys
import sqlite3

from Model.base import new_entry, get_entry, get_all, update, delete, filter_table
from Model.collaborateurs import collaborateurs_colonnes
from View.base import LOGIN_MENU, CRUD_MENU , affichage_menu, get_user_id, get_object_id, get_object_data


con = sqlite3.connect("database.db")
cur = con.cursor()

def quitter():
	con.close()
	sys.exit()


def connexion():
	id_utilisateur = get_user_id()
	profil_utilisateur = get_entry("collaborateurs", id_utilisateur)
	return profil_utilisateur


def inscription():
	data_utilisateur = get_object_data("collaborateur", collaborateurs_colonnes)
	""" if get_all("collaborateurs" == []):
		data_utilisateur = [("rowid", 1)] + data_utilisateur """
	profil_utilisateur = new_entry("collaborateurs", collaborateurs_colonnes, data_utilisateur)
	return profil_utilisateur


def login():
	options = {"1": "connexion", "2": "inscription", "3": "quitter"}
	menu_choisi = affichage_menu(LOGIN_MENU, options)
	if menu_choisi == "connexion":
		profil_utilisateur = connexion()
		return profil_utilisateur
	elif menu_choisi == "inscription":
		profil_utilisateur = inscription()
		return profil_utilisateur
	elif menu_choisi == "quitter":
		quitter()
	else :
		return 0

def accueil():
	show_login_page = True
	while show_login_page == True:
		profile_valide = login()
		if profile_valide :
			show_login_page = False
			return profile_valide
		else :
			print("Veuillez saisir une entrée valide")
		# login()

def ajouter(object_name, table_name, table_columns):
	raw_data = get_object_data(object_name, table_columns)
	data_list = [data[1] for data in raw_data]
	data_string = ", ".join(data_list)
	table_columns_string = ', '.join(table_columns)
	new_entry(table_name, table_columns_string, data_string)


def modifier(object_name, table_name, table_columns):
	object_id = get_object_id(object_name)
	print("Renseignez les nouvelles valeurs pour les colonnes à modifier ou tapez sur Entrée")
	raw_data = get_object_data(object_name, table_columns)
	data_list = [f"{data[0]} = {data[1]}" for data in raw_data if data[1]]
	data_string = ", ".join(data_list)
	update(table_name, object_id, data_string)


def operations_crud(object_name, table_name, table_columns):
	print(f"Ajouter, modifier, ou supprimer un {object_name}")
	options = {"1": "ajouter", "2": "modifier", "3": "supprimer", "4": "retour", }
	option_choisie = affichage_menu(CRUD_MENU, options)

	# while option_choisie != "retour" :

	if option_choisie == "ajouter":
		ajouter(object_name, table_name, table_columns)
		""" raw_data = get_object_data(object_name, table_columns)
		data_list = [data[1] for data in raw_data]
		data_string = ", ".join(data_list)
		table_columns_string = ', '.join(table_columns)
		new_entry(table_name, table_columns_string, data_string) """

	elif option_choisie == "modifier":
		modifier(object_name, table_name, table_columns)
		""" object_id = get_object_id(object_name)
		print("Renseignez les nouvelles valeurs pour les colonnes à modifier ou tapez sur Entrée")
		raw_data = get_object_data(object_name, table_columns)
		data_list = [f"{data[0]} = {data[1]}" for data in raw_data if data[1]]
		data_string = ", ".join(data_list)
		update(table_name, object_id, data_string) """

	elif option_choisie == "supprimer":
		object_id = get_object_id(object_name)
		delete(table_name, object_id)

	elif option_choisie == "retour":
		return "retour"

	else :
		return 0