from Model.base import new_entry, get_entry, get_all
from View.base import affichage_menu, get_object_id
from View.support import SUPPORT_MENU

def support_controller():
	options = {"1": "gestion-evenements", "2": "affichage-evenements",}
	menu_choisi = affichage_menu(SUPPORT_MENU, options)

	if menu_choisi == "gestion-evenements":
		id_utilisateur = get_object_id()
		profil_utilisateur = new_entry("collaborateurs", id_utilisateur)
	
	elif menu_choisi == "affichage-evenements":
		pass
	else :
		return 0