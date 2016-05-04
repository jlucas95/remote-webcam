#!/usr/bin/python3.4

from subprocess import Popen, PIPE, DEVNULL
import socket

HOST = "10.9.210.20"
PORT = 8000
while True:
    input("Press enter to take a picture")
    process = Popen(["fswebcam", "--quiet", "--no-banner", "-r", "1600x900", "--jpeg", "95",  "-"], stdout=PIPE, stderr=DEVNULL)
    image = process.stdout.read()
    print(image[:20])
    print(len(image))
    soc = socket.socket()
    soc.connect((HOST, PORT))
    soc.sendall(image)
    soc.close()
