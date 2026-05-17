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

def communicate_with_erlang_server(message, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as erlang_socket:
        erlang_socket.connect((host, port))
        erlang_socket.sendall(message.encode())
        erlang_socket.recv(1024).decode()
        erlang_socket.close
        response = erlang_socket.recv(1024).decode()
        print(f"Received from Erlang server: {response}")

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



# def run_command(command):
#     process = subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     return process

# def run_command(command, pid_queue):
#     process = subprocess.Popen(command, shell=True)
#     pid_queue.put(process.pid)
#     process.wait()

if __name__ == "__main__":
    message = "Hello, Servers!"
    host = "localhost"
    num_clients = 2
    
    command = "scaphandre json -n 100000000 -f report_100000.json"

    port_c = 54321  # Port for the C server
    port_erlang = 12345  # Port for the Erlang server

    c_threads = []
    erlang_threads = []

    # # Start the command in the background
    # process = run_command(command)

    # # Create a multiprocessing queue to share the PID
    # pid_queue = multiprocessing.Queue()

    # # Create a process to run the command
    # process = multiprocessing.Process(target=run_command, args=(command, pid_queue))
    # process.start()
    
    # # Start the command in the background
    # process = subprocess.Popen(command, shell=True)

    # # Wait for some time (e.g., 10 seconds)
    # time.sleep(10)

    # # Spawn a new process
    # process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    proc = subprocess.Popen(["scaphandre", "json", "-n", "100000000", "-f", "report_100000.json"])


    # # Get the PID of the newly spawned process
    # pid = process.pid
    # print(f"Newly spawned process PID: {pid}")
    print("starting measurement")

    # # Get the parent process
    # parent = psutil.Process(proc.pid)

    # Get the parent process
    parent = psutil.Process(proc.pid)
    


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

    print("killing")
    # Kill the child processes
    for child in parent.children(recursive=True):
        child.kill()

    # Kill the parent process
    parent.kill()

    # # Kill the process
    # os.kill(proc.pid, signal.SIGTERM)
    # # Kill the process
    # os.kill(proc.pid, signal.SIGKILL)

    # # Kill the process later (replace 'SIGTERM' with 'SIGKILL' if needed)
    # os.kill(pid, 15)  # 15 corresponds to the 'SIGTERM' signal

    print("Killed")


    # # Wait for the process to finish
    # process.wait()

    # Stop the process (if needed, replace 'stop' with the appropriate command)
    # process.terminate()


    # # Stop the process on Windows
    # if os.name == 'nt':
    #     subprocess.run(["taskkill", "/F", "/PID", str(process.pid)])
    # else:
    #     # On Unix-like systems, use the original termination code
    #     process.terminate()
    #     process.wait()

    # Get the process ID (PID) of the started command
    # pid = process.pid

    # # Stop the Python program
    # sys.exit()

    # Terminate the process by PID
    # try:
    #     # Get the process by PID
    #     process_to_terminate = psutil.Process(pid)

    #     # Terminate the process
    #     process_to_terminate.terminate()

    #     # Optionally, wait for the process to complete
    #     process_to_terminate.wait(timeout=5)
    # except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #     pass  # Process may have already terminated or cannot be terminated


    # # Kill the process using the PID
    # try:
    #     os.kill(pid, 15)  # 15 is the signal for SIGTERM (terminate)
    #     process.wait()  # Wait for the process to finish
    # except ProcessLookupError:
    #     print(f"Process with PID {pid} not found.")

        # Terminate the process and its children
    # try:
    #     parent = psutil.Process(process.pid)
    #     for child in parent.children(recursive=True):
    #         child.terminate()
    #     parent.terminate()
    #     process.wait()
    # except psutil.NoSuchProcess:
    #     pass


    # try:
    #     # Get the PID from the queue
    #     pid = pid_queue.get()

    #     # Get the process by PID
    #     process_to_terminate = psutil.Process(pid)

    #     # Terminate the process
    #     process_to_terminate.terminate()

    #     # Optionally, wait for the process to complete
    #     process_to_terminate.wait(timeout=5)
    # except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #     pass  # Process may have already terminated or cannot be terminated