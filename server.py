#!/usr/bin/env python
import socket, sys, re
from Crypto.Cipher import AES

# Usage
if len(sys.argv) <= 1:
    print "Usage: %s key" % sys.argv[0]
    exit(1)

key = sys.argv[1]
obj = AES.new(key, AES.MODE_ECB)

# Padding to encryption
# https://pythonexample.com/code/python-aes-ecb/
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)

HOST = 'localhost'
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

while 1:
    data = conn.recv(10240)
    if data == "q":
	exit(1)
	conn.close()

    # decrypt
    if re.match(r'^[0-9A-Fa-f]+$', data) != None:
        print obj.decrypt(data.decode("hex")) + "\r\n"
    # encrypt
    else:
	print obj.encrypt(pad(data)).encode("hex") + "\r\n"

conn.close()
