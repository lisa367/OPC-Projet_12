from Controller.base import accueil
from Controller.gestion import gestion_controller
from Controller.commercial import commercial_controller
from Controller.support import support_controller

def menu_selon_departement(profil_utilisateur):
	if profil_utilisateur(3) == "gestion":
		gestion_controller()
	elif profil_utilisateur(3) == "commercial":
		commercial_controller()
	elif profil_utilisateur(3) == "support":
		support_controller()
	else:
		return 0


def run_program():
	pass

if __name__ == "__main__":
	run_program()