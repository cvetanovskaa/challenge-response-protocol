import socket, sys
import hashlib
import pickle
import getpass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')
 
host = 'localhost'
port = 8000
s.connect((host , port))

def hashFunction(input):
	''' Used to return a hash value of the password+serverVal to be sent to the server'''
	h = hashlib.md5(input.encode())
	return h.hexdigest()

def send_val(data):
	''' Used to send data to the server ''' 
	try:
		s.sendall(data.encode("ASCII"))
	except socket.error:
		print ('Send failed')
		sys.exit()

def login_screen():
	login_register = "2"
	while login_register != "0" and login_register != "1" and login_register != "q":
		login_register = input("Please choose 1 to login to an existing account, and 0 to register. Press q to exit \n")
	if login_register == "1":
		return "login"
	elif login_register == "0":
		return "register"
	else:
		return "exit"

def main():
	''' The main driver of the program. It sends and receives data to the server in order to perform the authentication. '''

	while True:
		initiateLogin = login_screen()		
		if initiateLogin == "exit":
			break

		username = input("Please enter your username: ")
#		password = input("Please enter your password: ")
		password = getpass.getpass()
	
		if initiateLogin == "login":
			data = pickle.dumps((initiateLogin,username)) 
			s.sendall(data)
			reply = s.recv(1024)
			value_to_hash = hashFunction(password) + reply.decode("ASCII")
			hashed_val = hashFunction(value_to_hash)
			send_val(hashed_val)
			reply = s.recv(1024)
			reply = pickle.loads(reply)
			if reply[1] == 1 or reply[1] == 2:
				print(reply[0])
				break
			else:
				print (reply[0])
 
		else:
			hashed_pass = hashFunction(password)
			data = pickle.dumps((initiateLogin, username, hashed_pass))
			s.sendall(data)
			reply = s.recv(1024)
			print(reply.decode("ASCII"))
			print("You can login now using your credentials, or you can add another user.")

main()
