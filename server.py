import socket
import threading


class SocketServer(object):
    HOST = socket.gethostbyname('localhost')
    PORT = 65432
    addressTo = {}

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((SocketServer.HOST, SocketServer.PORT))
        self.data = ""
        self.trigger = None

    def listen(self):
        print("[+] Server started")
        self.sock.listen(5)
        conNum = 0
        while True:
            conNum += 1
            connection, address = self.sock.accept()
            # SocketServer.sendData.update({""})
            print(f"New connection from: {address}")
            SocketServer.addressTo.update({f"Connection{conNum}" : address})
            print(SocketServer.addressTo)
            threading.Thread(target=self.listenToClients, args=(connection, address)).start()

    def listenToClients(self, connection, address):
        buf_size = 1024
        while True:
            try:
                if address == SocketServer.addressTo["Connection1"]:
                    self.data = connection.recv(buf_size).decode()
                    if self.data:
                        print(self.data)
                        self.trigger = True
                if self.__len__() > 1 and address == SocketServer.addressTo["Connection2"]:
                    if self.trigger and "[+]New message from" in self.data:
                        connection.send(bytes(self.data, 'utf-8'))
                        self.trigger = False
                elif self.__len__() > 1 and address == SocketServer.addressTo["Connection3"]:
                    if self.trigger:
                        connection.send(bytes(self.data, 'utf-8'))
                        self.trigger = False
            except KeyboardInterrupt:
                quit()
            except Exception as error:
                print(f"[!] Connection closed from address: {address}")
                print(error)
                connection.close()
                return False

    def __len__(self):
        return len(SocketServer.addressTo)


server = SocketServer()
server.listen()
