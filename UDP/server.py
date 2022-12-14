import socket

HOST = "198.244.190.230" 
PORT = 65432

# TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    s.bind((HOST, PORT))
    
    while True:

        data, address = s.recvfrom(65507)
        
        if not data:
            break

        s.sendto(data, address)