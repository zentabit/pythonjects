import socket

sock = socket.socket()

host = "192.168.1.11"
port = 12345
sock.connect((host, port))
msg = input("What do you want to send? ")

sock.sendall(msg.encode('utf-8'))

sock.close()
