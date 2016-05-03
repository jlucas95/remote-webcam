#!/usr/bin/python3.4

import socket

soc = socket.socket()
soc.bind(("", 8000))
soc.listen(5)
sock, adrr_info = soc.accept()
recv_bytes = -1
file = open("network_image.jpg", "wb")
buffer = bytearray(4096)
total_bytes = 0
while recv_bytes != 0:
    recv_bytes = sock.recv_into(buffer)
    file.write(buffer[:recv_bytes])
    total_bytes += recv_bytes

print(total_bytes)
file.close()
soc.close()
