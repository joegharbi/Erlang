import json

# Specify the path to your JSON file
json_file_path = "c:\\phd\\Erlang\\report_C_100000_server.json"

# Read JSON data from the file
with open(json_file_path, "r") as file:
    data = json.load(file)

# Initialize total consumption variables
total_server_consumption = 0.0
total_erl_consumption = 0.0

# Iterate through entries
for entry in data:
    consumers = entry.get("consumers", [])
    for consumer in consumers:
        exe = consumer.get("exe", "")
        consumption = consumer.get("consumption", 0.0)
        
        # Check if the executable is "server.exe" or "erl.exe"
        if "a.exe" in exe.lower():
            total_server_consumption += consumption
        elif "erl.exe" in exe.lower():
            total_erl_consumption += consumption

# Print the results
print("Total consumption of server.exe:", total_server_consumption)
print("Total consumption of erl.exe:", total_erl_consumption)
