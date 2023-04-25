#!/usr/bin/env python3
# ipc_client.py

import socket
import random

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 9898        # The port used by the server

numbers = [random.randint(1,20)for _ in range(50)]
data = ",".join(str(num) for num in numbers)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data.encode())
    response = s.recv(1024)

print('Received', response.decode())
