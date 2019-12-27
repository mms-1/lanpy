import sys
import socket

s = socket.socket()
host = socket.gethostname()
port = 8899
print("Me (server): ", host, ":", port)
#s.bind((host, port))
s.bind(('', port))

s.listen(5)

while True:
	c, addr = s.accept()
	print("got connection from ", addr)
	msg = str("gg").encode()
	c.send(msg)
	c.close()
