import socket

sock = socket.socket()

host = socket.gethostname()
port = 12345
sock.bind((host, port))
sock.listen(5)
print("Ready...")

while True:
    m, conn = sock.accept()
    print(m.recv(1024))


sock.close()
