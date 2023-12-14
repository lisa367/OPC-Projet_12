import sqlite3

con = sqlite3.connect("database.db")
cur = con.cursor()

def new_entry(table, table_columns, data):
	new_row = tuple(data)
	print(new_row)
	table_columns_string = ', '.join(table_columns)
	num_marks = ["?" for column in table_columns]
	placeholders = ", ".join(num_marks)
	command = f"""INSERT INTO {table} ({table_columns_string}) VALUES({placeholders})"""
	# print(command)
	cur.execute(command, new_row)
	id = cur.lastrowid
	# new = cur.lastrow
	con.commit()
	print('dernier id: %d' % id)
	# print('nouvelle ligne : %d' % new)

	return id

def new_entries(table, table_columns, data):
	new_row = tuple(data)
	table_columns_string = ', '.join(table_columns)
	num_marks = ["?" for item in table_columns]
	placeholders = " ".join(num_marks)
	command = f"""INSERT INTO {table} ({table_columns_string}) VALUES({placeholders})"""
	print(command)
	cur.executemany(command, new_row)
	id = cur.lastrowid
	# new = cur.lastrow
	con.commit()
	print('dernier id: %d' % id)
	# print('nouvelle ligne : %d' % new)

	return id


def get_entry(table, id):
	command = f"""SELECT * FROM {table} WHERE rowid = {id}"""
	query = cur.execute(command)
	return query.fetchone()

def get_all(table):
	command = f"""SELECT rowid, * FROM {table}"""
	query = cur.execute(command)
	return query.fetchall()
		
def update(table, id, data):
	command = f"UPDATE {table} SET {data} WHERE rowid={id}"
	cur.execute(command)
	con.commit()

def delete(table, id):
	command = f"DELETE FROM {table} WHERE rowid={id}"
	cur.execute(command)
	con.commit()
	print("Successfully deleted")
	

def filter_table(table, columns=None, conditions=None):
		columns_names = columns if columns else "*"
		command = f"SELECT {columns_names} FROM {table}"
		# command = f""select {columns if columns else '*'} from {table}""
		if conditions :
			command = command + f"WHERE {conditions}"

		query = cur.execute(command)
		return query.fetchall()

    
# con.close()


""" def filter_table(table, columns=None, conditions=None):
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
 """