'''
 The client is receving a random hashed value from the server & combining it with the password the user enters.
 Then, that is being sent to the server. If it matches the value that the server gets, then the authentication is valid.
'''
import socket, sys, time
from Crypto.Cipher import AES

listening_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sending_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ADDRESS, PORT = '127.0.0.1', 8000
listening_sock.connect((ADDRESS, PORT+1))
sending_sock.connect((ADDRESS,PORT))

def hashFunction(input):
	''' Used to return a hash value of the password & the password+serverVal '''
	return hash(input)

def getHashVal():
# 	message = listening_sock.recv(1024)  
# 	message = message.decode('ASCII')
# 	return message


# def Tcp_Read( ):
	a = ' '
	b = ''
	while a != '\n':
		a = listening_sock.recv(1)
		b = b + a
	return b

def sendData(data):
	data = data + "\n"
	sending_sock.send(data.encode('ASCII'))
	return

def main():
	#Maybe make a login/registration part?

	uname = input("Enter your username")
	passw = input("Enter your password")
	sendData("")
	print("A")
	serverVal = getHashVal()
	print(serverVal)
	finalHashVal = hashFunction(serverVal + passw)

	send((uname,finalHashVal))

main()
