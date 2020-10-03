
import csv

fields_name = ['client','TV A','TV B']

list = {"client": "blabla",
        'TV A' : 5 ,
        'TV B': 1000}

def add_new_line_to_csv(new_line):
    with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv', 'a') as file:
        writer = csv.DictWriter(file, fieldnames=fields_name)
        writer.writerow(new_line)

add_new_line_to_csv(list)