from communication_class import Client
from matrix_lite import sensors
import pickle
import time

board = Client()

board.create_socket()
board.create_connection()

_to_send = dict()
_to_send['accel_x'] = 0.0
_to_send['accel_y'] = 0.0
_to_send['accel_z'] = 0.0
_to_send['gyro_x'] = 0.0
_to_send['gyro_y'] = 0.0
_to_send['gyro_z'] = 0.0
_to_send['mag_x'] = 0.0
_to_send['mag_y'] = 0.0
_to_send['mag_z'] = 0.0
_to_send['yaw'] = 0.0
_to_send['pitch'] = 0.0
_to_send['roll'] = 0.0


while True:
    _reading = sensors.imu.read()
    _to_send['accel_x'] = _reading.accel_x
    _to_send['accel_y'] = _reading.accel_y
    _to_send['accel_z'] = _reading.accel_z
    _to_send['gyro_x'] = _reading.gyro_x
    _to_send['gyro_y'] = _reading.gyro_y
    _to_send['gyro_z'] = _reading.gyro_z
    _to_send['mag_x'] = _reading.mag_x
    _to_send['mag_y'] = _reading.mag_y
    _to_send['mag_z'] = _reading.mag_z
    _to_send['yaw'] = _reading.yaw
    _to_send['pitch'] = _reading.pitch
    _to_send['roll'] = _reading.roll
    
    x = input()
    
    if x == "exit":
        board.send(board.DISCONNECT_MESSAGE.encode(board.FORMAT))
        break
    
    message = pickle.dumps(_to_send)

    print(type(message))

    board.send(message)

    board.send(board.DISCONNECT_MESSAGE.encode(board.FORMAT))
    break
    