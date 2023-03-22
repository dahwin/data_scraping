import csv

# Read the CSV file containing the list of integers
with open('qproxy.csv', 'r') as input_file:
  reader = csv.reader(input_file)
  int_list = [row[0] for row in reader]

# Convert the list of integers to a list of strings
string_list = [str(i) for i in int_list]

# Write the list of strings to a new CSV file
with open('output.csv', 'w', newline='') as output_file:
  writer = csv.writer(output_file)
  writer.writerows([[string] for string in string_list])