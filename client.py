#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    text = raw_input("")
    s.sendall(text)
    if text == "q":
	exit(1)
	s.close()

s.close()
