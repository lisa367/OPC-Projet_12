import os
import sys
import sqlite3

from Model.base import new_entry, get_entry, get_all, update, delete, filter_table
from Model.collaborateurs import collaborateurs_colonnes
from View.base import LOGIN_MENU, CRUD_MENU, TABLE_MENU, affichage_menu, get_user_id, get_object_id, get_object_data


con = sqlite3.connect("database.db")
cur = con.cursor()

def has_permission(table_name, table_columns, filter_column, object_id, user_id):
	entry = get_entry(table_name, object_id)
	entry_zipped = zip(table_columns, entry)
	entry_dict = {column: value for column, value in entry_zipped}


def ajouter(object_name, table_name, table_columns, default_values=None):
	# print("INITIAL : ",table_columns)
	if default_values:
		# default_values = liste de tuples de type (colonne, valeur_par_defaut)
		values_index = {}
		new_table_columns = [label for label in table_columns]
		# print(table_columns)
		for value_tuple in default_values:
			index = table_columns.index(value_tuple[0])
			values_index[index] = value_tuple
			new_table_columns.remove(value_tuple[0])
		raw_data = get_object_data(object_name, new_table_columns)

		for i in range(len(table_columns)+1):
			if i in values_index.keys():
				raw_data.insert(i, values_index[i])
		print(raw_data)

	else: 
		raw_data = get_object_data(object_name, table_columns)

	values_list = [int(data[1]) if data[1].isdigit() else data[1] for data in raw_data]
	# data_string = ", ".join(values_list)
	# table_columns_string = ', '.join(table_columns)
	# print("Before save : ",table_columns)
	new_id = new_entry(table_name, table_columns, values_list)
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
			ajouter(object_name, table_name, table_columns, default_values)

		elif option_choisie == "modifier":
			modifier(object_name, table_name, table_columns)

		elif option_choisie == "supprimer":
			object_id = get_object_id(object_name)
			delete(table_name, object_id)

		elif option_choisie == "retour":
			show_crud_menu = False

		else :
			print("Veuillez saisir une entrée valide")


def afficher_table():
	table_choisie = affichage_menu(TABLE_MENU, {"1": "clients", "2": "contrats", "3": "evenements"})
	if table_choisie in ["clients", "contrats", "evenements"]:
		query_result = get_all(table_choisie)
		print(query_result)
	else:
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

