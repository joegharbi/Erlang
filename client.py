import socket
# import sys
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

if __name__ == "__main__":
    # if len(sys.argv) != 4:
    #     print("Usage: python client.py <message> <host>")
    #     sys.exit(1)

    # message = sys.argv[1]
    # host = sys.argv[2]
    # num_clients =  int(sys.argv[3]) # Number of clients for each server
    
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 10000

    port_c = 54321  # Port for the C server
    port_erlang = 12345  # Port for the Erlang server

    c_threads = []
    erlang_threads = []

    

    for i in range(1, num_clients + 1):
        c_thread = threading.Thread(target=c_client_thread, args=(message, host, port_c))
        erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        
        c_threads.append(c_thread)
        erlang_threads.append(erlang_thread)

        c_thread.start()
        erlang_thread.start()

    # Wait for all threads to complete
    for c_thread, erlang_thread in zip(c_threads, erlang_threads):
        c_thread.join()
        erlang_thread.join()
