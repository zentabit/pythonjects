import socket
import threading

server = socket.socket()

ip = '0.0.0.0'
port = 12345

server.bind((ip, port))
server.listen(5)


def handler(client_socket):
	request = client_socket.recv(1024)

	print('Recieved: %s' % request.decode())

	client_socket.send('ACK!'.encode())
	client_socket.close()

while True:
	client, address = server.accept()
	print('Accepted connection from %s:%d' % (address[0], address[1]))
	client_handler = threading.Thread(target=handler, args=(client, ))
	client_handler.start()

