#UDPServer.py

import socket #Importação do módulo "socket" em Python

HOST = 'localhost' # Definição de endereço do host
PORT = 50000 # porta do socket atribuida para o serviço

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Definição de IPV4 e Tipo 
																# UDP para transporte
serverSocket.bind ((HOST, PORT)) # Vinculo do endereço IP e porta dos socket
print ('Aguardando conexão com o cliente')

while 1:

	message, clientAddress = serverSocket.recvfrom(2048)
	print ('Conected to:', clientAddress)
	print ('Mesagem recebida', message)
	modifiedMessage = message.upper()
	print ('Mensagem modificada:', modifiedMessage)
	serverSocket.sendto(modifiedMessage, clientAddress)


