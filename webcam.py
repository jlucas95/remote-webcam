#!/usr/bin/python3.4
"""
Creates a picture using the webcam and sends it over a socket
"""

from subprocess import Popen, PIPE, DEVNULL
import socket
import ssl
HOST = "IP"
PORT = 0

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
while True:
    input("Press enter to take a picture")
    process = Popen(["fswebcam", "--quiet", "--no-banner", "-r", "1600x900", "--jpeg", "95", "-"],
		stdout=PIPE, stderr=DEVNULL)
    image = process.stdout.read()
    image_len = str(len(image))
    print("{0} bytes captured".format(image_len))
    soc = socket.socket()
    sslsoc = context.wrap_socket(soc)
    sslsoc.connect((HOST, PORT))
    sslsoc.sendall(image)
    sslsoc.close()
