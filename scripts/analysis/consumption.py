import json
import os

# Specify the path to your directory containing JSON files
directory_path = "c:\\phd\\Erlang\\"


# current_directory = os.getcwd()


# Initialize total consumption variables
total_server_consumption = 0.0
total_erl_consumption = 0.0

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".json"):
        json_file_path = os.path.join(directory_path, filename)

        # Read JSON data from the file
        with open(json_file_path, "r") as file:
            data = json.load(file)

        # Iterate through entries
        for entry in data:
            consumers = entry.get("consumers", [])
            for consumer in consumers:
                exe = consumer.get("exe", "")
                consumption = consumer.get("consumption", 0.0)

                # Check if the executable is "server_old.exe" or "erl.exe"
                if "server_old.exe" in exe.lower():
                    total_server_consumption += consumption
                elif "erl.exe" in exe.lower():
                    total_erl_consumption += consumption

# Print the results
print("Total consumption of server_old.exe:", total_server_consumption)
print("Total consumption of erl.exe:", total_erl_consumption)
