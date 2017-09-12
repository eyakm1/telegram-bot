import socket
import threading


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('10.0.13.110', 20000))
    sock.listen(1)
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('Accepted connection from', client_address)
            while True:
                data = connection.recv(1024)
                if data:
                    print(str(data, 'UTF-8'))
        finally:
            connection.close()



def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting to server....')
    server_address = ('10.0.2.100', 20000)
    print ('Connecting to', '', 'port' , 20000)
    sock.connect(server_address)
    try:
        while True:
            message = bytes(input(), 'UTF-8')
            sock.sendall(message)
    finally:
        sock.close()


e1 = threading.Event()
e2 = threading.Event()


t1 = threading.Thread(target=server, args=())
t2 = threading.Thread(target=client, args=())

t1.start()

t = input()

t2.start()

e1.set()

t2.join()
t1.join()