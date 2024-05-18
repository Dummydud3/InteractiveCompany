import socket
import time

# Host and port for the server
SERVER_HOST = '127.0.0.1'  # IP address of the server
SERVER_PORT = 8082  # Port number where the server is listening

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))
print(f'Connected to server at {SERVER_HOST}:{SERVER_PORT}')

# Send messages to the server
messages = ["executeKillPlayer", "executeOtherAction"]  # Example messages
for message in messages:
    client_socket.sendall(message.encode())
    print(f'Sent message to server: {message}')
    time.sleep(1)  # Add a delay between messages

# Close the connection
client_socket.close()
