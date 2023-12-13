import os
import sentry_sdk
from Controller.base import accueil, retreive_user_profile
from Controller.gestion import gestion_controller
from Controller.commercial import commercial_controller
from Controller.support import support_controller


def menu_selon_departement(profil_utilisateur):
	if profil_utilisateur["departement"].lower() == "gestion":
		gestion_controller()
	elif profil_utilisateur["departement"].lower() == "commercial":
		commercial_controller()
	elif profil_utilisateur["departement"].lower() == "support":
		support_controller()
	else:
		return 0


def run_program():
	""" sentry_sdk.init(
    dsn="https://a09900948fc542f2e4474a0f0e5e66a4@o4506244442554368.ingest.sentry.io/4506377879289856",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
) """
	# division_by_zero = 1 / 0
	accueil()
	USER_ID = int(os.getenv("USER_ID"))
	logged_in_user = retreive_user_profile(USER_ID)
	print(f"User profile : {logged_in_user}")
	menu_selon_departement(logged_in_user)

if __name__ == "__main__":
	run_program()
