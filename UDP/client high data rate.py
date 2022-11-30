import socket

HOST = "198.244.190.230"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    s.settimeout(2)
    s.connect((HOST, PORT))
    
    # Send Hello World to the server in a loop for 1000000 times
    for i in range(1000000):
        s.sendall(b"Hello")
        s.sendall(b"World")
    
    while True:  

        data = s.recv(65507)

        data = data.decode("utf-8")

        print(f"{data}")