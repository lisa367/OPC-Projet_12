import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

contrats_colonnes = ["client_id", "contact_commercial", "montant_facture", "montant_redevable", "date_creation", "statut", "collaborateur_id"]


def create_table_contrats():
		cur.execute("""CREATE TABLE IF NOT EXISTS contrats(
					contact_commercial TEXT,
					montant_facture REAL, 
					montant_redevable TEXT,
					date_creation TEXT,
                    statut TEXT DEFAULT 'non-signé',
			  		client_id INTEGER, 
			  		collaborateur_id INTEGER,
			  		FOREIGN KEY(client_id) REFERENCES clients(rowid),
			  		FOREIGN KEY(collaborateur_id) REFERENCES collaborateurs(rowid)
)
""")

con.commit()