import sys
import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

LOGIN_MENU = """
1 - Connexion
2 - Inscription
3 - Quitter
"""

CRUD_MENU = """
1 - Ajouter
2 - Modifier
3 - Supprimer
4 - Retour
"""

GENERAL_MENU = """
Recherchez :
1 - Un (des) client(s)
2 - Un (des) contrat(s)
3 - Un (des) évènements(s)
"""

def affichage_menu(nom_menu, options_menu):
	print(nom_menu)
	choix_option = input("Veuillez choisir une option : ")
	return options_menu.get(choix_option, 0)

def get_user_id():
	id_utilisateur = input("Veuillez renseigner votre identifiant : ")
	return id_utilisateur

def quitter():
	con.close()
	sys.exit()

def get_object_id(object_name):
	if object_name == "evenment":
		id_objet = input("Veuiller renseigner l'identifiant de l'évènement")
	else:
		id_objet = input(f"Veuiller renseigner l'identifiant du {object_name}")
	return id_objet


def get_object_data(object_name, table_columns):
	object_data = []
	print(f"Veuillez renseigner les données du nouveau {object_name} ")
	for column in table_columns:
		data = input(f"Valeur pour la colonne '{column}' : ")
		object_data.append((column, data))
	return object_data


def get_query_conditions():
	stop = False
	conditions = []
	while not stop:
		ajout = input("Ajouter une condition ? oui ou non : ")
		if ajout.lower() == "oui":
			if condition :
				AND_or_OR = input("AND ou OR").strip()
				while AND_or_OR not in ["AND", "OR"]:
					pass
			condition = input("Renseignez votre condition : ")
		else:
			stop = True
	return conditions

def get_query_filters(table_columns):
	columns_names = ", ".join(table_columns)
	print(f"""Colonnes de la table :\n{columns_names})""")
	selected_columns = input("Veuillez renseigner les colonnes à afficher, séparées d'un espace")
	conditions_list = get_query_conditions()
	selected_conditions = " ".join(conditions_list)
	

"""
def login_menu():
	options = {"1": "connexion", "2": "inscription", "3": "quitter"}
	print(LOGIN_MENU)
	choix_option = input("Veuillez choisir une option (1, 2, ou 3) : ")
	return options.get(choix_option, 0)
"""