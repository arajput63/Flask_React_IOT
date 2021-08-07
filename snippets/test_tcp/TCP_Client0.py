# echo taken out, this sends multiple streams of data back to the server only.
import socket
from time import sleep

TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "&HELLO, MANY WORLDS!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_IP = socket.gethostname()
s.connect((socket_IP, TCP_PORT))
for x in range(5):
    s.send(str.encode(str(x) + " " + MESSAGE, "utf-8"))
    print("Message send via Socket:", socket_IP, ":", TCP_PORT)
    sleep(0.5)
s.close()