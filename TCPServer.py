#TCPServer.py

import socket

HOST = 'localhost'
PORT = 50000

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((HOST,PORT))

serverSocket.listen()
print ("Aguardando conexão do cliente...")
conn, ender = serverSocket.accept()

print ('Conectado com:', ender)

cont = 0
while 1:
	data = conn.recv(2048)
	string = data.decode()

	if cont == 0:
		guarda = 0

	if (string == 'rec') & (guarda == 0):

		data = str.encode('Não há o que recuperar. Ainda nao foram enviados dados')
		print ('Ainda não recebemos dados para recuperação')
		conn.sendall(data)
		guarda = 0

	elif (string == 'rec') & (guarda != 0):

		print ('Mensagem recuperada:', guarda)
		conn.sendall(guarda)

	elif string != 'rec':

		guarda = data
		print ('Mensagem recebida:', data)
		conn.sendall(data)

	cont+=1

	


