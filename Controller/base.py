import os
import sys
import sqlite3

from Model.base import new_entry, get_entry, get_all, update, delete, filter_table
from Model.collaborateurs import collaborateurs_colonnes
from View.base import LOGIN_MENU, CRUD_MENU , affichage_menu, get_user_id, get_object_id, get_object_data


con = sqlite3.connect("database.db")
cur = con.cursor()

def ajouter(object_name, table_name, table_columns, default_values=None):
	if default_values:
		# default_values = liste de tuples de type (colonne, valeur_par_defaut)
		values_index = {}
		new_table_columns = table_columns

		for value_tuple in default_values:
			index = table_columns.index(value_tuple[0])
			values_index[index] = value_tuple
			new_table_columns.remove(value_tuple[0])
		raw_data = get_object_data(object_name, new_table_columns)

		for i in len(table_columns):
			if i in values_index.keys():
				raw_data.insert(i, values_index[i])
		print(raw_data)

	else: 
		raw_data = get_object_data(object_name, table_columns)

	data_list = [data[1] for data in raw_data]
	data_string = ", ".join(data_list)
	# table_columns_string = ', '.join(table_columns)
	new_id = new_entry(table_name, table_columns, data_list)
	return new_id


def modifier(object_name, table_name, table_columns):
	object_id = get_object_id(object_name)
	print("Renseignez les nouvelles valeurs pour les colonnes à modifier ou tapez sur Entrée.")
	raw_data = get_object_data(object_name, table_columns)
	data_list = [f"{data[0]} = '{data[1]}'" for data in raw_data if data[1]]
	data_string = ", ".join(data_list)
	print(data_list)
	print(data_string)
	update(table_name, object_id, data_string)



def operations_crud(object_name, table_name, table_columns, default_values=None):
	show_crud_menu = True
	while show_crud_menu :
		print(f"Ajouter, modifier, ou supprimer un {object_name}")
		options = {"1": "ajouter", "2": "modifier", "3": "supprimer", "4": "retour", }
		option_choisie = affichage_menu(CRUD_MENU, options)

		if option_choisie == "ajouter":
			ajouter(object_name, table_name, table_columns, default_values=None)

		elif option_choisie == "modifier":
			modifier(object_name, table_name, table_columns)

		elif option_choisie == "supprimer":
			object_id = get_object_id(object_name)
			delete(table_name, object_id)

		elif option_choisie == "retour":
			show_crud_menu = False

		else :
			print("Veuillez saisir une entrée valide")


def quitter():
	con.close()
	sys.exit()


def connexion():
	id_utilisateur = get_user_id()
	utilisateur_inscrit = get_entry("collaborateurs", id_utilisateur)
	if utilisateur_inscrit:
		return id_utilisateur
	else:
		return 0


def login_menu():
	options = {"1": "connexion", "2": "quitter"}
	menu_choisi = affichage_menu(LOGIN_MENU, options)
	if menu_choisi == "connexion":
		id_utilisateur = connexion()
		return id_utilisateur
	elif menu_choisi == "quitter":
		quitter()
	else :
		return 0
	

def accueil():
	show_login_page = True
	while show_login_page == True:
		id_valide = login_menu()
		if id_valide :
			os.environ["USER_ID"] = id_valide
			show_login_page = False
			print("USER_ID : ", os.getenv("USER_ID"))
			return id_valide
		else :
			print("Veuillez saisir une entrée valide")
		# login()


def retreive_user_profile(id_valide):
	data_utilisateur = list(get_entry("collaborateurs", id_valide))
	data_liste = zip(collaborateurs_colonnes, data_utilisateur)
	profile_utilisateur = {item[0]: item[1] for item in data_liste}
	return profile_utilisateur


"""
def inscription():
	nouvel_id_utilisateur = ajouter("collaborateur", "collaborateurs", collaborateurs_colonnes)
	# data_utilisateur = get_object_data("collaborateur", collaborateurs_colonnes)
	# if get_all("collaborateurs" == []):
	# 	data_utilisateur = [("rowid", 1)] + data_utilisateur
	# collaborateurs_colonnes_string = ", ".join(collaborateurs_colonnes)
	# nouvel_id_utilisateur = new_entry("collaborateurs", collaborateurs_colonnes_string, data_utilisateur)
	return nouvel_id_utilisateur


def login():
	options = {"1": "connexion", "2": "quitter"}
	menu_choisi = affichage_menu(LOGIN_MENU, options)
	if menu_choisi == "connexion":
		id_utilisateur = connexion()
		return id_utilisateur
	elif menu_choisi == "inscription":
		id_utilisateur = inscription()
		return id_utilisateur
	elif menu_choisi == "quitter":
		quitter()
	else :
		return 0


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
		# raw_data = get_object_data(object_name, table_columns)
		# data_list = [data[1] for data in raw_data]
		# data_string = ", ".join(data_list)
		# table_columns_string = ', '.join(table_columns)
		# new_entry(table_name, table_columns_string, data_string)

	elif option_choisie == "modifier":
		modifier(object_name, table_name, table_columns)
		# object_id = get_object_id(object_name)
		# print("Renseignez les nouvelles valeurs pour les colonnes à modifier ou tapez sur Entrée")
		# raw_data = get_object_data(object_name, table_columns)
		# data_list = [f"{data[0]} = {data[1]}" for data in raw_data if data[1]]
		# data_string = ", ".join(data_list)
		# update(table_name, object_id, data_string)

	elif option_choisie == "supprimer":
		object_id = get_object_id(object_name)
		delete(table_name, object_id)

	elif option_choisie == "retour":
		return "retour"

	else :
		return 0
"""