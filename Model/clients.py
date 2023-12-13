import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

clients_colonnes = ["nom_complet", "email", "telephone", "nom_entreprise", "date_premier_contact", "date_dernier_contact", "collaborateur_id",]


def create_table_clients():
		cur.execute("""CREATE TABLE IF NOT EXISTS clients(
					nom_complet TEXT, 
					email TEXT,
					telephone TEXT, 
					nom_entreprise TEXT,
					date_premier_contact TEXT,
                    date_dernier_contact TEXT,
                    contact_commercial TEXT,
			  		collaborateur_id INTEGER,
			  		FOREIGN KEY(collaborateur_id) REFERENCES collaborateurs(rowid)
)
""")

con.commit()