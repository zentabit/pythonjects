import os
import json
import socket


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def sendmsg(h):
    try:
        print("Setting up...")
        sock = socket.socket()
        sock.connect((h, 12345))
        print("Done.")
        b = json.dumps(input("Message: ")).encode()
        sock.sendall(b)
        sock.close()
    except ConnectionError:
        print("Couldn't establish conn, sorry.")
    except TimeoutError:
        print("Couldn't establish, conn timed out.")
        input("Enter to continue.")
    except OSError:
        print("Bad host, try again")
        input("Enter to continue...")


def recvmsg():
    sock = socket.socket()
    sock.bind((socket.gethostname(), 12345))
    sock.listen(1)
    m, conn = sock.accept()
    tmp = 0
    while True:
        tmp = m.recv(1024)
        break
    tmp = tmp.decode()
    print(json.loads(tmp))
    sock.close()


while True:
    cls()
    print(30 * "-")
    print("MAIN MENU")
    print(30 * "-")
    print("\n")
    print("1. Send a message.")
    print("2. Receive a message.")
    print("3. Test connection")
    print("4. Exit")
    choice = input("Select option [1-4]: ")
    try:
        choice = int(choice)
        if choice == 1:
            print("Sending mode.")
            host = input("IP to host: ")
            sendmsg(host)
        elif choice == 2:
            print("Transmission follows.")
            recvmsg()
            try:
                input("Transmission end.")
            except SyntaxError:
                pass
        elif choice == 3:
            print("I have crippling depression")
            input()
        elif choice == 4:
            print("Exiting")
            break
        else:
            print("Sorry, couldn't find that")
    except ValueError:
        print("I didn't catch that, try again.")
