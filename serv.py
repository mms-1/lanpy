# import sys
import socket
from threading import Thread
import configparser
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='server.log',
                    filemode='a',
                    format='[%(asctime)-15s] %(name)s - %(levelname)s - %(message)s')

config = configparser.ConfigParser()
config.read('config.ini')
generalConfig = config['General']

ss = socket.socket()
host = socket.gethostname()
port = int(generalConfig['port'])

print("Me (server): ", host, ":", port)
ss.bind(('', port))
logging.info('=== NEW SESSION ===')


class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            msg = self.sock.recv(1024).decode()
            print('Client(', self.addr, ') sent:', msg)
            logging.info('Client(%s %s ) sent: %s', self.addr, self.sock, msg)
            self.sock.send(b'kk')


ss.listen(5)
print('server started and listening...')
while 1:
    cs, address = ss.accept()
    print("got connection from ", address)
    logging.info('Got connection from %s %s', cs, address)
    Client(cs, address)

ss.close()
cs.close()
