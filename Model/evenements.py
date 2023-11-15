import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

evenements_colonnes = ["nom_complet", "email", "telephone", "nom_entreprise", "date_premier_contact", "date_dernier_contact", "collaborateur_ref",]


def create_table():
		# command = f"""CREATE TABLE IF NOT EXISTS {employees}(
					# title, year, score)"""
		cur.execute("""CREATE TABLE IF NOT EXISTS contrats(
					nom_evenement INTEGER FOREIGN KEY,
                    lieu TEXT,
                    id_contrat INTEGER FOREIGN KEY, 
                    nom_client TEXT,
					email_client TEXT,
					telephone_client TEXT, 
					date_debut TEXT,
                    date_fin TEXT,
                    nombre_invites INTEGER,
                    commentaires TEXT,
                    contact_support TEXT,
			  		collaborateur_ref INTEGER FOREIGN KEY
)
""")

con.commit()