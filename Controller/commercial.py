from Model.base import new_entry, get_entry, get_all, quitter
from View.base import affichage_menu, get_object_id
from View.commercial import COMMERCIAL_MENU

def commercial_controller():
	options = {"1": "clients", "2": "gestion-contrats", "3": "affichage-contrats", "4": "evenements"}
	menu_choisi = affichage_menu(COMMERCIAL_MENU, options)
	if menu_choisi == "clients":
		id_utilisateur = get_object_id()
		# id_utilisateur = get_user_id()
		profil_utilisateur = new_entry("collaborateurs", id_utilisateur)
	elif menu_choisi == "gestion-contrats":
		pass
	elif menu_choisi == "affichage-contrats":
		pass
	elif menu_choisi == "evenements":
		pass
	else :
		return 0