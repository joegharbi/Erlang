import socket
import subprocess
import signal
import psutil
import os
import sys
import time
import threading
import multiprocessing


def communicate_with_erlang_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as erlang_socket:
        erlang_socket.connect((host, port))
        erlang_socket.sendall(message.encode())
        erlang_socket.recv(1024).decode()
        erlang_socket.close
        # erlang_socket.recv(1024).decode()
        # response = erlang_socket.recv(1024).decode()
        # print(f"Received from Erlang server: {response}")


def erlang_client_thread(message, host, port_erlang):
    # print(f"Erlang Client sending message: {message}")
    communicate_with_erlang_server(message, host, port_erlang)

if __name__ == "__main__":
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 10000
    
    command = "scaphandre json -n 100000 -f report_Erlang_10000.json"

    process = subprocess.Popen(command, shell= True)

    time.sleep(10)

    port_erlang = 12345  # Port for the Erlang server

    erlang_threads = []
    
    # Start Erlang threads concurrently
    for i in range(1, num_clients + 1):
        erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        erlang_threads.append(erlang_thread)
        erlang_thread.start()
        time.sleep(0.1)
    
    # Wait for all Erlang threads to complete
    for erlang_thread in erlang_threads:
        erlang_thread.join()

    # Then kill the process
    subprocess.run(f'taskkill /F /IM scaphandre.exe', shell=True)

    # # Get process details as dictionary
    # for proc in psutil.process_iter():
    #     pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
    #     # Check if process name matches the command
    #     if pinfo['name'] == 'scaphandre.exe':
    #         # Kill the process
    #         os.kill(pinfo['pid'], signal.SIGTERM)
    #         print(f"Killed process {pinfo['pid']}")

    # Exit the program
    sys.exit()