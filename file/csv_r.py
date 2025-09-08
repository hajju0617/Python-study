import csv

with open('C:\\Python-study\\PB\\output.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
