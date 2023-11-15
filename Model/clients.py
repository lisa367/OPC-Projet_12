import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

clients_colonnes = ["nom_complet", "email", "telephone", "nom_entreprise", "date_premier_contact", "date_dernier_contact", "collaborateur_ref",]


def create_table():
		# command = f"""CREATE TABLE IF NOT EXISTS {employees}(
					# title, year, score)"""
		cur.execute("""CREATE TABLE IF NOT EXISTS contrats(
					nom_complet INTEGER FOREIGN KEY, 
					email TEXT,
					telephone TEXT, 
					nom_entreprise TEXT,
					date_premier_contact TEXT,
                    date_dernier_contact TEXT,
                    contact_commercial TEXT,
			  		collaborateur_ref INTEGER FOREIGN KEY
)
""")

con.commit()