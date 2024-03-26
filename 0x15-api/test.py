#!/usr/bin/python3
import csv

# Sample data
data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]

# File path to save the CSV
file_path = 'data.csv'

# Write data to CSV file
with open(file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{file_path}' has been created successfully.")

