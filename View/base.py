import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

LOGIN_MENU = """
1 - Connexion
2 - Quitter
"""

CRUD_MENU = """
1 - Ajouter
2 - Modifier
3 - Supprimer
4 - Retour
"""

TABLE_MENU = """
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


def get_object_id(object_name):
	if object_name == "evenment":
		id_objet = input("Veuiller renseigner l'identifiant de l'évènement")
	else:
		id_objet = input(f"Veuiller renseigner l'identifiant du {object_name} : ")
	return id_objet


def get_object_data(object_name, table_columns):
	object_data = []
	# object_data = {}
	print(f"Veuillez renseigner les données du nouveau {object_name} : ")
	for column in table_columns:
		data = input(f"Valeur pour la colonne '{column}' : ")
		object_data.append((column, data))
		# object_data[column] = data
	#print(object_data)
	return object_data


def get_query_conditions():
	stop = False
	conditions = []
	while not stop:
		ajout = input("Ajouter une condition ? oui ou non : ")
		if ajout.lower() == "oui":
			if conditions:
				AND_or_OR = input("AND ou OR : ").strip()
				while AND_or_OR not in ["AND", "OR"]:
					print("Veuillez saisir une entrée valide. ")
					AND_or_OR = input("AND ou OR").strip()
				condition = input("Renseignez votre condition : ")
			else:
				condition = input("Renseignez votre condition : ")
				"""AND_or_OR = input("AND ou OR : ").strip()
				 	while AND_or_OR not in ["AND", "OR"]:
					print("Veuillez saisir une entrée valide. ")
					AND_or_OR = input("AND ou OR : ").strip() 
				condition = input("Renseignez votre condition : ")"""
		else:
			stop = True
	return conditions

def get_query_filters(table_columns):
	print(f"""Colonnes de la table :\n{table_columns})""")
	selected_columns_raw = input("Veuillez renseigner les colonnes à afficher, séparées d'un espace : ")
	selected_columns = ", ".join(selected_columns_raw.split(" "))
	conditions_list = get_query_conditions()
	selected_conditions = " ".join(conditions_list)
	return selected_columns, selected_conditions


def add_or_modify(object):
	action = input(f"Add (1) or modify (2) {object}. Enter 1 or 2 :")
	return action
