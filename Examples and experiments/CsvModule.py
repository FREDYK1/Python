import csv

with open("Temperatures.csv", 'r') as file:
    data = list(csv.reader(file))
print(data)
region = input("Enter your region: ")

for row in data[1:]:
    if row[0] == region:
        print(row[1])
