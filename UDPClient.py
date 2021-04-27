#UDPClient.py

import socket

HOST = '127.0.0.1'
PORT = 50000

opc = 0

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
	message = input('Insira a sua mensagem em minúsculo: ')

	clientSocket.sendto(str.encode(message),(HOST, PORT))
	modifiedMessage, serverAdress = clientSocket.recvfrom(2048)

	print ('mensagem de volta:', modifiedMessage.decode())
	

	

	


