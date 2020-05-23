import socket


class ClientSocket(object):
    HOST = socket.gethostbyname('localhost')
    PORT = 65432

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def reciveMessages(self):
        self.sock.connect((ClientSocket.HOST, ClientSocket.PORT))
        print("[+]Connected to server.")
        while True:
            data = self.sock.recv(1024).decode()
            if data:
                print(data)


client = ClientSocket()
client.reciveMessages()