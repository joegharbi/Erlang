import socket

# Create a socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c_socket:
    # Connect to the server
    c_socket.connect(("localhost", 6000))

    # Send a message
    c_socket.sendall(b"Hello, Server!")

    # Indicate that no more data will be sent
    c_socket.shutdown(socket.SHUT_WR)

    # Receive any response from the server (optional)
    response = c_socket.recv(1024)
    print(f"Received from Java server: {response}")
