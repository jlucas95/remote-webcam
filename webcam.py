#!/usr/bin/python3.4

from subprocess import Popen, PIPE, DEVNULL
import socket

HOST = "192.168.2.5"
PORT = 8000

process = Popen(["fswebcam", "--quiet", "--no-banner", "-r", "1600x900", "--jpeg", "95",  "-"], stdout=PIPE, stderr=DEVNULL)
image = process.stdout.read()
soc = socket.socket()
soc.connect((HOST, PORT))
soc.sendall(image)
soc.close()
