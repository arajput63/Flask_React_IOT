# simply code to serve TCP data in python

import socket
import sys

TCP_IP = '0.0.0.0'  # local host needed?
TCP_PORT = 5005
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), TCP_PORT))
s.listen(5)

conn, addr = s.accept()
print('Connection address:', addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("Socket:", TCP_IP, ":", TCP_PORT)
    data_string = str(data)
    data_array = data_string.split("&")
    print("sys: " + str(sys.getsizeof(data)))
    print("len: " + str(len(data)))
    print("received data:", data)
    slice_count = 0
    for data_slice in data_array:
        print("data slice " + str(slice_count) + ":", data_slice)
        slice_count += 1
conn.close()
