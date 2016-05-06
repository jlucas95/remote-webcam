#!/usr/bin/python3.4

import socket
import datetime

FORMAT = "jpg"

soc = socket.socket()
soc.bind(("", 8000))
soc.listen(5)
while True:
    sock, adrr_info = soc.accept()
    recv_bytes = -1
    timestamp = str(datetime.datetime.now())
    file_name = "images/{0}.{1}".format(timestamp, FORMAT)
    file = open(file_name, "wb")
    buffer = bytearray(4096)
    total_bytes = 0
    while recv_bytes != 0:
        recv_bytes = sock.recv_into(buffer)
        file.write(buffer[:recv_bytes])
        total_bytes += recv_bytes
    print("{0} bytes written to file {1}".format(total_bytes, file_name))
file.close()
soc.close()

