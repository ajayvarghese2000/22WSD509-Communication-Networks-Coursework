import socket

HOST = "198.244.190.230"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    # Send Hello World 100 times to the server
    for i in range(100):

        s.sendall(b"Hello World")
        
    # Receive the data from the server
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Received {data!r}")
