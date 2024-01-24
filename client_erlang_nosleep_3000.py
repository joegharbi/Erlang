import csv
import os
import socket
import subprocess
import sys
import time
import threading
import json
import timeit
# import multiprocessing
# import signal
# import psutil
# import os

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

    num_clients = 3000
    server_name = "erl"
    file_name = f"report_{server_name}_{num_clients}"

    # Start Erlang server
    erl_server_command =  "erl -noshell -run echo_server_prod"
    erl_proc = subprocess.Popen(erl_server_command, shell=True)
    time.sleep(5)
    
    # scaphandre json -s 0 -n 100000 -m 100 -f
    # command = "scaphandre json -n 100000000 -m 100 -f report_C_100000.json"
    command = "scaphandre json -n 100000 -f "+file_name+".json"
    process = subprocess.Popen(command,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell= True)
    time.sleep(5)

    port_erlang = 12345  # Port for the Erlang server

    erlang_threads = []
    start_time = timeit.default_timer()
    
    # Start Erlang threads concurrently
    for i in range(1, num_clients + 1):
        erlang_thread = threading.Thread(target=erlang_client_thread, args=(message, host, port_erlang))
        erlang_threads.append(erlang_thread)
        erlang_thread.start()
        # time.sleep(0.1)
    
    # Wait for all Erlang threads to complete
    for erlang_thread in erlang_threads:
        erlang_thread.join()

    end_time = timeit.default_timer()

    # runtime = end_time - start_time - (num_clients * 0.1)
    runtime = end_time - start_time

    # Then kill the process
    subprocess.run(f'taskkill /F /IM scaphandre.exe', shell=True)
    # # Then kill the process
    subprocess.run(f'taskkill /F /IM erl.exe', shell=True)

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
            if f"{server_name}.exe" in exe.lower():
                total_server_consumption += consumption
                number_samples +=1
    if (number_samples != 0):
        average_energy = total_server_consumption / number_samples

    final_consumption = average_energy * runtime

    # Print the results
    # print("Total consumption of server_old.exe:", total_server_consumption)

    # Write runtime and function name to the csv file
    with open('erlang_output_nosleep.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        # csv_writer.writerow(['Function', 'Average Runtime'])
        csv_writer.writerow([file_name, final_consumption, runtime])

    # # Open the file in write mode ('w')
    # with open(file_name+'.txt', 'w') as f:
    #     # Write to the text file
    #     f.write(f"The runtime of {file_name} is: {runtime} seconds\n")
    #     f.write(f"Total consumption of {server_name}: {total_server_consumption}\n")
    #     f.write(f"Total samples of {server_name}: {number_samples}\n")
    #     f.write(f"Average consumption of {server_name}: {average_energy}\n")
        

    # Exit the program
    sys.exit()