import socket
import subprocess
import sys
import time
import threading
import json
# import multiprocessing
# import signal
# import psutil
# import os

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
    
    num_clients = 100
    server_name = "c_server_win"
    file_name = f"report_{server_name}_{num_clients}"
    
    # scaphandre json -s 0 -n 100000 -m 100 -f
    # command = "scaphandre json -n 100000000 -m 100 -f report_C_100000.json"
    command = "scaphandre json -n 100000 -f "+file_name+".json"
    process = subprocess.Popen(command,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell= True)
    time.sleep(5)

    port_c = 54321  # Port for the C server

    c_threads = []    
    start_time = time.time()

    # Start C threads
    for i in range(1, num_clients + 1):
        c_thread = threading.Thread(target=c_client_thread, args=(message, host, port_c))
        c_threads.append(c_thread)
        c_thread.start()
        time.sleep(0.1)


    # Wait for all C threads to complete
    for c_thread in c_threads:
        c_thread.join()

    end_time = time.time()

    runtime = end_time - start_time - (num_clients * 0.1)

    # print(f"The runtime of your code is: {runtime} seconds")

    # Then kill the process
    subprocess.run(f'taskkill /F /IM scaphandre.exe', shell=True)

    json_file_path = f"c:\\phd\\Erlang\\{file_name}.json"

    # Read JSON data from the file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Initialize total consumption variables
    total_server_consumption = 0.0
    number_samples = 0
    average_energy = 0

    # Iterate through entries
    for entry in data:
        consumers = entry.get("consumers", [])
        for consumer in consumers:
            exe = consumer.get("exe", "")
            consumption = consumer.get("consumption", 0.0)
            
            # Check the server consumption
            # if f"{server_name}.exe" in exe.lower() and consumption != 0.0:
            if f"{server_name}.exe" in exe.lower():
                total_server_consumption += consumption
                number_samples +=1
    if (number_samples != 0):
        average_energy = total_server_consumption / number_samples

    # Print the results
    # print("Total consumption of server_old.exe:", total_server_consumption)

    # Open the file in write mode ('w')
    with open(file_name+'.txt', 'w') as f:
        # Write to the text file
        f.write(f"The runtime of {file_name} is: {runtime} seconds\n")
        f.write(f"Total consumption of {server_name}: {total_server_consumption}\n")
        f.write(f"Total samples of {server_name}: {number_samples}\n")
        f.write(f"Average consumption of {server_name}: {average_energy}\n")
        

    # Exit the program
    sys.exit()