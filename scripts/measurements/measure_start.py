import subprocess
import sys
import time
import threading
import json

if __name__ == "__main__":

    # if len(sys.argv) != 4:
    #     print("Usage: python measure_start.py <message> <host>")
    #     sys.exit(1)

    # message = sys.argv[1]
    # host = sys.argv[2]
    # num_clients =  int(sys.argv[3]) # Number of clients for each server

    num_clients = 10
    server_name = "erl"
    file_name = f"report_{server_name}_{num_clients}"
    
    # scaphandre json -s 0 -n 100000 -m 100 -f
    # command = "scaphandre json -n 100000000 -m 100 -f report_C_100000.json"
    command = "scaphandre json -n 100000 -f "+file_name+".json"
    process = subprocess.Popen(command,stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell= True)
    time.sleep(5)

    port_erlang = 12345  # Port for the Erlang server

    erlang_threads = []
    start_time = time.time()
    
    # Start measurement
    # execute


    end_time = time.time()

    runtime = end_time - start_time

    # Then kill the process
    subprocess.run(f'taskkill /F /IM scaphandre.exe', shell=True)

    json_file_path = f"c:\\phd\\Erlang\\{file_name}.json"

    # Read JSON data from the file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Initialize total consumption variables
    total_server_consumption = 0.0
    number_samples = 0

    # Iterate through entries
    for entry in data:
        consumers = entry.get("consumers", [])
        for consumer in consumers:
            exe = consumer.get("exe", "")
            consumption = consumer.get("consumption", 0.0)
            
            # Check the server consumption
            if f"{server_name}.exe" in exe.lower() and consumption != 0.0:
                total_server_consumption += consumption
                number_samples +=1

    # Print the results
    # print("Total consumption of server_old.exe:", total_server_consumption)

    # Open the file in write mode ('w')
    with open(file_name+'.txt', 'w') as f:
        # Write to the text file
        f.write(f"The runtime of {file_name} is: {runtime} seconds\n")
        f.write(f"Total consumption of {server_name}: {total_server_consumption}\n")
        f.write(f"Total samples of {server_name}: {number_samples}\n")
        

    # Exit the program
    sys.exit()