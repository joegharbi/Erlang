import csv

# Read the data from the CSV file
with open('data.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    data = list(reader)

# Create a dictionary to store the energy consumption and runtime for C for each condition
c_values = {}
for row in data:
    if row[0] == 'c':
        condition = (row[1], int(row[2]))  # The condition is a tuple of sleep/no_sleep and number of clients
        c_values[condition] = (float(row[3]), float(row[4]))  # Store the energy consumption and runtime

# Normalize the data
for row in data:
    condition = (row[1], int(row[2]))
    if condition in c_values:
        c_energy, c_runtime = c_values[condition]
        row[3] = str(float(row[3]) / c_energy if c_energy else 'NA')  # Normalize energy consumption
        row[4] = str(float(row[4]) / c_runtime if c_runtime else 'NA')  # Normalize runtime

# Write the normalized data to a new CSV file
with open('normalized_data.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(data)
