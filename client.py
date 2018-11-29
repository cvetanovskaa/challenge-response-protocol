import socket, sys
import hashlib
import pickle

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
def main():
	''' The main driver of the program. It sends and receives data to the server in order to perform the authentication. '''
	username = input("Please enter your username: ")
	password = input("Please enter your password: ")
	
	while True:
		initiateLogin = "login"
		send_val(initiateLogin)
		reply = s.recv(1024)
		value_to_hash = password + reply.decode("ASCII")
		hashed_val = hashFunction(value_to_hash)
		print(hashed_val)
		send_val(hashed_val)
		reply = s.recv(1024)
		reply = pickle.loads(reply)
		if reply[1] == 1 or reply[1] == 2:
			print(reply[0])
			break
		else:
			print (reply[0]) 

main()
