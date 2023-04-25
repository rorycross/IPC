#!/usr/bin/env python3
# ipc_server.py

import socket
import statistics as st

HOST = '0.0.0.0'  
# 0.0.0.0 is a non-routable meta-address that also specifies all IP # addresses on all interfaces on the system
PORT = 9898        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            numbers = [int(num) for num in data.decode().split(",")]
            print("Received:", numbers)
            
            mean = st.mean(numbers)
            median = st.median(numbers)
            stdev = st.stdev(numbers)
            
            results = f"Mean: {mean: .2f}, Median: {median: .2f}, Standard Deviation: {stdev: .2f}"
            
            conn.sendall(results.encode())
            print(results)
