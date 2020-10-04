
import csv

# fields_name = ['client','TV A','TV B']

# list = {"client": "blabla",
#         'TV A' : 5 ,
#         'TV B': 1000}

# def add_new_line_to_csv(new_line):
#     with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv', 'a') as file:
#         writer = csv.DictWriter(file, fieldnames=fields_name)
#         writer.writerow(new_line)

# add_new_line_to_csv(list)


# Essayer une fois de faire une classe, de la créer et de pushed les données dans le CSV
class Shop:
        def __init__ (self, client, tv_a, tv_b):
                self.client = client
                self.tv_a = tv_a
                self.tv_b = tv_b
        def add_new_line_to_csv(self):
                fields_name = ['client','tv_a','tv_b']
                list2 = self.__dict__
                # list = {"client": "blabla", 'tv_a' : 5 ,'tv_b': 1000}
                with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv', 'a', newline='') as file:
                        writer = csv.DictWriter(file, fieldnames=fields_name)
                        writer.writerow(list2)
                # print(list)
                print(list2)

client = Shop("blabla",11,11)
client.add_new_line_to_csv()
