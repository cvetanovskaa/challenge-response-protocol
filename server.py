import socket
import sqlite3
import sys

HOST, PORT = '127.0.0.1', 8000

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))

send_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
send_sock.bind((HOST, PORT+1))

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

def Tcp_Read():
	a = ' '
	b = ''
	#import pdb
	#pdb.set_trace()
	while a != '\n':
		a = listen_socket.recv(1)
		b = b + a
	return b

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
	

	# making 

	listen_socket.listen(1)

	while True:
	    # Wait for a connection
	    print(sys.stderr, 'waiting for a connection')
	    connection, client_address = listen_socket.accept()
	    print("SS ", connection, client_address)
	    option = Tcp_Read()
	    option = option.strip('\n') 
	    print(option)
	    
	    try:
	        print(sys.stderr, 'connection from', client_address)

	        # Receive the data in small chunks and retransmit it
	        while True:
	            data = connection.recv(16)
	            print(sys.stderr, 'received "%s"' % data)
	            if data:
	                print(sys.stderr, 'sending data back to the client')
	                connection.sendall(data)
	            else:
	                print(sys.stderr, 'no more data from', client_address)
	                break
	            
	    finally:
	        # Clean up the connection
	    	connection.close()

main()
