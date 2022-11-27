import socket

HOST = "198.244.190.230"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(5)
    s.connect((HOST, PORT))
    s.sendall(b"Hello world " * 100)
    s.sendall(b"Last")
    
    
    while True:  
        data = s.recv(4024)

        data = data.decode("utf-8")

        print(f"{data}")