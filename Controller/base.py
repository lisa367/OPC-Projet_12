from Model.base import new_entry, get_entry, get_all, update, delete, filter_table
from View.base import LOGIN_MENU, CRUD_MENU , affichage_menu, get_user_id, quitter, get_object_id, get_object_data


def login():
	options = {"1": "connexion", "2": "inscription", "3": "quitter"}
	menu_choisi = affichage_menu(LOGIN_MENU, options)
	if menu_choisi == "connexion":
		id_utilisateur = get_user_id()
		profil_utilisateur = new_entry("collaborateurs", id_utilisateur)
		return profil_utilisateur
	elif menu_choisi == "inscription":
		pass
	elif menu_choisi == "quitter":
		quitter()
	else :
		return 0

def accueil():
	login_page = login()
	while login_page == 0:
		print("Veuillez saisir une entrée valide")
		login()

def operations_crud(object_name, table_name, table_columns):
	print(f"Ajouter, modifier, ou supprimer un {object_name}")
	options = {"1": "ajouter", "2": "modifier", "3": "supprimer", "4": "retour", }
	option_choisie = affichage_menu(CRUD_MENU, options)

	# while option_choisie != "retour" :

	if option_choisie == "ajouter":
		object_data = get_object_data(object_name, table_columns)
		new_object = new_entry(table_name, object_name)
		# fonction pour sauvegarder la nouvelle entrée
	elif option_choisie == "modifier":
		object_id = get_object_id(object_name)
		object_data = get_object_data(table_name, object_name)
		update(table_name, object_id, object_data)
	elif option_choisie == "supprimer":
		object_id = get_object_id(object_name)
		delete(table_name, object_id)
	elif option_choisie == "retour":
		pass
	else :
		return 0