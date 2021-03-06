import socketio #to install dependency with pip, use - pip install "python-socketio[client]"
import datetime
import time

from subprocess import check_output

server_address = "localhost" # insert server IP address here
#server_port = 5000
server_port = 80

sio = socketio.Client()

@sio.event
def connect():
    print("[ INFO ] Incoming connection from something...?")

@sio.event
def connect_error():
    print("[ INFO ] Failed to connect.")

@sio.event
def disconnect():
    print("[ INFO ] Disconnected from the server.")


print('[ INFO ] Connecting to server http://{}:{}...'.format(
    server_address, server_port))


def get_ip_addr():
    return check_output(['hostname', '-I']).decode().rstrip()

server_connected = False

def ping_server():
    global server_connected
    print('Sending ping request to server...')
    sio.emit(
        'PING_FROM_CLIENT',
        {
            'picam_ip': get_ip_addr()
        },
        namespace='/client')
    server_connected = False

@sio.on('PING_FROM_SERVER', namespace='/client')
def ping_response(message):
    global server_connected
    print('Ping response received: ' + message['server_ip'])
    server_connected = True


sio.connect(
    'http://{}:{}'.format(server_address, server_port),
    transports=['websocket'],
    namespaces=['/client']
)

while True:
    ping_server()
    time.sleep(5)