import socket
import subprocess
import signal
import psutil
import os
import sys
import time
import threading
import multiprocessing

def communicate_with_c_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c_socket:
        c_socket.connect((host, port))
        c_socket.sendall(message.encode())
        c_socket.recv(1024)
        # response = c_socket.recv(1024)
        # print(f"Received from C server: {response}")

def c_client_thread(message, host, port_c):
    # print(f"C Client sending message: {message}")
    communicate_with_c_server(message, host, port_c)

if __name__ == "__main__":
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 10000
    
    # scaphandre json -s 0 -n 100000 -m 100 -f
    # command = "scaphandre json -n 100000000 -m 100 -f report_C_100000.json"
    command = "scaphandre json -n 100000 -f report_c_win_10000_server.json"

    process = subprocess.Popen(command, shell= True)

    time.sleep(10)

    port_c = 54321  # Port for the C server

    c_threads = []    

    # Start C threads
    for i in range(1, num_clients + 1):
        c_thread = threading.Thread(target=c_client_thread, args=(message, host, port_c))
        c_threads.append(c_thread)
        c_thread.start()
        time.sleep(0.1)


    # Wait for all C threads to complete
    for c_thread in c_threads:
        c_thread.join()

    # Then kill the process
    subprocess.run(f'taskkill /F /IM scaphandre.exe', shell=True)

    # When you want to exit the program, call sys.exit()
    sys.exit()