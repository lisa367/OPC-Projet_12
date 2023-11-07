import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

def new_entry(table, data):
		new_row = tuple(data)
		command = """INSERT INTO {table} VALUES(?)"""
		cur.executemany(command, new_row)
		id = cur.lastrowid
		# new = cur.lastrow
		con.commit()
		print('dernier id: %d' % id)
		# print('nouvelle ligne : %d' % new)
		return id


def get_entry(table, id):
		command = f"""SELECT * FROM {table} WHERE {id}"""
		query = cur.execute(command)
		return query.fetchone()

def get_all(table):
		command = f"""SELECT * FROM {table}"""
		query = cur.execute(command)
		return query.fetchall()
		
def update(table, id, data):
	command = f"UPDATE {table} SET {data} WHERE id={id}"
	cur.execute(command)

def delete(table, id):
	command = f"DELETE {table} WHERE id={id}"
	cur.execute(command)

def filter_table(table, columns=None, conditions=None):
	# command = f""SELECT {columns if columns else '*'} FROM {table}""
    if columns:
        # command = f""SELECT {columns} FROM {table}""
        command = ''
	else :
		# command = f""SELECT * FROM {table}""
        command = ''	
	if conditions :
		command = command + f"WHERE {conditions}"
	query = cur.execute(command)
	return query.fetchall()


con.close()