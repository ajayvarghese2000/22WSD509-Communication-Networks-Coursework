import socket

HOST = "198.244.190.230"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.settimeout(2)
    s.connect((HOST, PORT))
    
    # Send Hello World to the server
    s.send(b"Hello")
    s.send(b"World")

    while True:  
        data = s.recv(1024)

        data = data.decode("utf-8")

        print(f"{data}")

