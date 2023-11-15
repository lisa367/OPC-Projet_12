import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

contrats_colonnes = ["prenom", "nom", "departement", "role", "email",]


def create_table():
		# command = f"""CREATE TABLE IF NOT EXISTS {employees}(
					# title, year, score)"""
		cur.execute("""CREATE TABLE IF NOT EXISTS contrats(
					nom_complet INTEGER FOREIGN KEY, 
					email TEXT,
					telephone REAL, 
					nom_entreprise TEXT,
					date_premier_contact TEXT,
                    date_dernier_contact TEXT DEFAULT 'non-signé',
                    contact_commercial TEXT,
			  		collaborateur_ref INTEGER FOREIGN KEY
)
""")

con.commit()