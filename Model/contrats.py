import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

contrats_colonnes = ["prenom", "nom", "departement", "role", "email",]


def create_table():
		# command = f"""CREATE TABLE IF NOT EXISTS {employees}(
					# title, year, score)"""
		cur.execute("""CREATE TABLE IF NOT EXISTS contrats(
					client_id INTEGER FOREIGN KEY, 
					contact_commercial TEXT,
					montant_facture REAL, 
					montant_redevable TEXT,
					date_creation TEXT,
                    statut TEXT DEFAULT 'non-signé',
			  		collaborateur_id INTEGER FOREIGN KEY
)
""")

con.commit()