#TCPClient.py

import socket

HOST = 'localhost'
PORT = 50000

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((HOST, PORT))

while 1:

	message = input("Entre com os dados: ")
	clientSocket.sendto(str.encode(message),(HOST, PORT))
	modifiedMessage, serveAdress = clientSocket.recvfrom(2048)

	print ('Mensagem ecoada:', modifiedMessage.decode())
