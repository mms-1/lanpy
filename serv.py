# import sys
import socket
from threading import Thread
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
generalConfig = config['General']

ss = socket.socket()
host = socket.gethostname()
port = int(generalConfig['port'])

print("Me (server): ", host, ":", port)
ss.bind(('', port))


class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client(', self.addr, self.sock, ') sent:', self.sock.recv(1024).decode())
            self.sock.send(b'Oi you sent something to me')


ss.listen(5)
print('server started and listening...')
while 1:
    cs, address = ss.accept()
    print("got connection from ", address)
    Client(cs, address)

ss.close()
cs.close()
