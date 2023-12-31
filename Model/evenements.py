import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

evenements_colonnes = ["nom_evenement", "lieu", "contrat_id", "nom_client", "email_client", "telephone_client", "date_debut", "date_fin", "nombre_invites", "commentaires", "contact_support", "support_collaborateur_id", ]


def create_table_evenements():
		cur.execute("""CREATE TABLE IF NOT EXISTS evenements(
					nom_evenement TEXT,
                    lieu TEXT, 
                    nom_client TEXT,
					email_client TEXT,
					telephone_client TEXT, 
					date_debut TEXT,
                    date_fin TEXT,
                    nombre_invites INTEGER,
                    commentaires TEXT,
                    contact_support TEXT,
			  		contrat_id INTEGER, 
			  		support_collaborateur_id INTEGER,
			  		FOREIGN KEY(contrat_id) REFERENCES contrats(rowid),
			  		FOREIGN KEY(support_collaborateur_id) REFERENCES collaborateurs(rowid)
)
""")

con.commit()