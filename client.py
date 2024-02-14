import socket

# Define host and port
HOST = '127.0.0.1'  # localhost
PORT = 12345        # Arbitrary non-privileged port

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    # Connect to server
    client_socket.connect((HOST, PORT))

    while True:
        # Input command to send to server
        command = input("Enter command (e.g., 'book 1', 'available', 'schedule', 'exit'): ")
        if command.lower() == 'exit':
            break
        # Send the command to server
        client_socket.sendall(command.encode())
        # Receive response from server
        response = client_socket.recv(1024)
        print('Server response:', response.decode())
