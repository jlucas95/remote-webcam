#!/usr/bin/python3.4

from subprocess import Popen, PIPE, DEVNULL
import socket

HOST = "localhost"
PORT = 8000
while True:
    input("Press enter to take a picture")
    process = Popen(["fswebcam", "--quiet", "--no-banner", "-r", "1600x900", "--jpeg", "95", "-"], stdout=PIPE, stderr=DEVNULL)
    image = process.stdout.read()
    image_len = str(len(image))
    print("{0} bytes captured".format(image_len))
    soc = socket.socket()
    soc.connect((HOST, PORT))
    soc.sendall(image)
    soc.close()
