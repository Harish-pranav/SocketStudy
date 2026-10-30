import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print(f"Client connected from: {client_socket.getsockname()}")
    server_message = client_socket.recv(1024).decode()
    print(f"Received from server: {server_message}")
    client_socket.sendall(b"Acknowledgement received from the client.")
