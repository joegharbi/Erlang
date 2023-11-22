import socket
# import sys
import time
import threading

def communicate_with_c_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c_socket:
        c_socket.connect((host, port))
        c_socket.sendall(message.encode())
        c_socket.recv(1024)
        # response = c_socket.recv(1024)
        # print(f"Received from C server: {response}")

def communicate_with_erlang_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as erlang_socket:
        erlang_socket.connect((host, port))
        erlang_socket.sendall(message.encode())
        erlang_socket.recv(1024).decode()
        erlang_socket.close
        # response = erlang_socket.recv(1024).decode()
        # print(f"Received from Erlang server: {response}")

def c_client_thread(message, host, port_c):
    # print(f"C Client sending message: {message}")
    communicate_with_c_server(message, host, port_c)

def erlang_client_thread(message, host, port_erlang):
    # print(f"Erlang Client sending message: {message}")
    communicate_with_erlang_server(message, host, port_erlang)

# if __name__ == "__main__":
#     message = "Hello, Servers!"
#     host = "localhost"
#     num_clients = 100000

#     port_c = 54321  # Port for the C server
#     port_erlang = 12345  # Port for the Erlang server

#     for i in range(1, num_clients + 1):
#         c_thread = threading.Thread(target=c_client_thread, args=(message, host, port_c))
#         erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        
#         c_thread.start()
#         c_thread.join()  # Wait for the C thread to complete before starting the next pair

#         erlang_thread.start()
#         erlang_thread.join()  # Wait for the Erlang thread to complete


if __name__ == "__main__":
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 100000

    port_c = 54321  # Port for the C server
    port_erlang = 12345  # Port for the Erlang server

    c_threads = []
    erlang_threads = []

    # Start C threads
    for i in range(1, num_clients + 1):
        c_thread = threading.Thread(target=c_client_thread, args=(message, host, port_c))
        c_threads.append(c_thread)
        c_thread.start()
        time.sleep(0.1)
        # print(threading.active_count())

    # Start Erlang threads concurrently
    for i in range(1, num_clients + 1):
        erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        erlang_threads.append(erlang_thread)
        erlang_thread.start()
        time.sleep(0.1)
    
    
    # print(threading.active_count())
    # print(threading.enumerate())


    # Wait for all C threads to complete
    for c_thread in c_threads:
        c_thread.join()


    # Wait for all Erlang threads to complete
    for erlang_thread in erlang_threads:
        erlang_thread.join()



