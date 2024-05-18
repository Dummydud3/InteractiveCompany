import socket
import time

# Host and port for the BepInEx plugin
PLUGIN_HOST = '127.0.0.1'  # IP address of the BepInEx plugin
PLUGIN_PORT = 7885  # Port number where the plugin is listening for UDP packets

# Create a UDP socket for the plugin connection
plugin_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f'Connecting to BepInEx plugin at {PLUGIN_HOST}:{PLUGIN_PORT}')

# Keep attempting to send data to the plugin until successful
while True:
    try:
        # Send a test message to check if the plugin is reachable
        plugin_socket.sendto(b'Test message', (PLUGIN_HOST, PLUGIN_PORT))
        print(f'Connected to BepInEx plugin at {PLUGIN_HOST}:{PLUGIN_PORT}')
        break  # Break the loop if connection successful
    except ConnectionRefusedError:
        print(f'Connection to BepInEx plugin at {PLUGIN_HOST}:{PLUGIN_PORT} failed. Retrying in 5 seconds...')
        time.sleep(5)  # Wait for 5 seconds before retrying

# Create a TCP socket for the server (for receiving messages from the plugin)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind(('127.0.0.1', 8082))

# Listen for incoming connections
server_socket.listen()

print('Server listening on 127.0.0.1:8082')

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')

    # Receive data from the client (executed Python script)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # Print received data
        print(f'Received message from Python script: {data.decode()}')

        # Forward the message to the BepInEx plugin
        plugin_socket.sendto(data, (PLUGIN_HOST, PLUGIN_PORT))

    # Close the connection
    client_socket.close()
