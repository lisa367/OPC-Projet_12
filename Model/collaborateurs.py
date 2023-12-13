import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

collaborateurs_colonnes = ["prenom", "nom", "departement", "role", "email",]


def create_table_collaborateurs():
		cur.execute("""CREATE TABLE IF NOT EXISTS collaborateurs(
					prenom TEXT, 
					nom TEXT,
					departement TEXT, 
					role TEXT,
					email TEXT
)
""")

con.commit()