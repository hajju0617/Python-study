import csv

data = [
    ['Name', 'Email', 'Phone'], ['John Doe', 'johndoe@example.com', '123-456-7890']
       ]

with open('output.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    for row in data:
        csv_writer.writerow(row)
