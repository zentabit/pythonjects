import socket
import winsound
print(socket.gethostbyname(socket.gethostname()) + " on " + socket.gethostname())
winsound.Beep(1000, 50000)
input()