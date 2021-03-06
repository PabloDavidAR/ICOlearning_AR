import socket
import time
from matrix_lite import sensors


HEADER = 64
PORT = 5100     #Same as Server
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.10"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    # We need to check if the message is 64 bytes lengths
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
time.sleep(1)
send(DISCONNECT_MESSAGE)

while True:
	print("IMU values: ")
	print(sensors.imu.read())
	time.sleep(1)

