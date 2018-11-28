import socket
import sqlite3

HOST, PORT = 'localhost', 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))

unames = [("subedir", "berea2015"), ("karkig", "berea2016"), ("scottw", "college201"),("alex", "berea2018"), ("vasant","berea2010"),
 ("peter", "berea2011"), ("ronaldo", "realmadrid"), ("messi", "barcelona"), ("neymar", "psg2017")]

def create_connection(db_file):
	""" create a database connection to the SQLite database
		specified by db_file
		:param db_file: database file
		:return: Connection object or None
	"""
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print(e)
	return None

def create_table(conn, query):
	""" create a table from the create_table_sql statement
		:param conn: Connection object
		:param create_table_sql: a CREATE TABLE statement
		:return:
	"""
	try:
		c = conn.cursor()
		c.execute(query)
	except Error as e:
		print(e)

def add_user(db, username, password):
	conn = create_connection(db)
	cursor = conn.cursor()
	for uname in unames:
		cursor.execute('insert into usernames (username, password) values (?, ?)', (uname[0], uname[1],))
#		cursor.execute('insert into usernames (name, password) values (?, ?)', (username, password,))
	conn.commit() 	

def main():

	db = "users.db"
	conn = create_connection(db)

	sql_query = """ CREATE TABLE IF NOT EXISTS usernames(
			id integer primary key AUTOINCREMENT,
			username nvarchar(40) not null,
			password nvarchar(32) not null
		); """
	
	if conn is not None:
		create_table(conn, sql_query)
#		add_user(db, "","")
	else:
		print("Error! cannot create the database connection.")

	while True:
		
	
		
main()
