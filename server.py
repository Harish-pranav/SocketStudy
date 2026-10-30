import socket

HOST = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("Server is waiting for a connection...", flush=True)
    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}", flush=True)
        conn.sendall(b"Hello from the server!")
        data = conn.recv(1024)
        print(f"Received from client: {data.decode()}", flush=True)
