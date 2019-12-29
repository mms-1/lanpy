import socket
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
generalConfig = config['General']
port = int(generalConfig['port'])
host = generalConfig['host']

playerConfig = config['Player']
nick = playerConfig['nick']

s = socket.socket()
localhost = socket.gethostname()

print("Me:", localhost, '\nName:', nick)

print("Connecting to:", host, ':', port)
s.connect((host, port))


def ts(msg):
    s.send(msg.encode())
    data = ''
    data = s.recv(1024).decode()
    print(data)


while 1:
    r = input('enter: ')
    ts(r)

s.close()
