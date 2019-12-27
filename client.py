import socket
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
genConfig = config['General']
port = int(genConfig['port'])
host = genConfig['host']

s = socket.socket()
localhost = socket.gethostname()

print("Me: ", localhost)

print("Connecting to:", host, ':', port)
s.connect((host, port))
msg = s.recv(1024).decode()
print(msg)
s.close()
