import socket
from poorconn import make_socket_patchable, delay_before_sending_upon_acceptance

HOST = "198.244.190.230" 
PORT = 65432

# TCP socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s = make_socket_patchable(s)
    delay_before_sending_upon_acceptance(s, 20, 1024)
    s.bind((HOST, PORT))
    s.listen()
    
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)