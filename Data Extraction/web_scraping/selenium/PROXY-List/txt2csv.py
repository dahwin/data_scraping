import csv

# Read the list of IP addresses and ports from the text file
with open('proxy.txt', 'r') as file:
    proxy_list = [line.strip() for line in file]

# Define the CSV file name
csv_file = 'proxy.csv'

# Write the proxy list to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    for proxy in proxy_list:
        writer.writerow([proxy])

print(f"Proxy list has been saved to {csv_file}")
