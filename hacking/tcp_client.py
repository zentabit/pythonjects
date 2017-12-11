import socket

client = socket.socket()

client.connect(('127.0.0.1', 12345))
client.send("HEy it works!".encode())

print(client.recv(4096))

