import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connection Address:', addr)
while True:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("Received data:", data)
    conn.send(data) # echo
conn.close()
