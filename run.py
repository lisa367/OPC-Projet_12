import sentry_sdk
from Controller.base import accueil
from Controller.gestion import gestion_controller
from Controller.commercial import commercial_controller
from Controller.support import support_controller


def menu_selon_departement(profil_utilisateur):
	if profil_utilisateur[3] == "gestion":
		gestion_controller()
	elif profil_utilisateur[3] == "commercial":
		commercial_controller()
	elif profil_utilisateur[3] == "support":
		support_controller()
	else:
		return 0


def run_program():
	sentry_sdk.init(
    dsn="https://a09900948fc542f2e4474a0f0e5e66a4@o4506244442554368.ingest.sentry.io/4506377879289856",
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
)
	# division_by_zero = 1 / 0
	accueil()

if __name__ == "__main__":
	run_program()
