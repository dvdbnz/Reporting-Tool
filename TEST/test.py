import csv

def database_as_array():
    database = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv')
    survey = database.read()
    database.close()
    survey = survey.split("\n")
    return survey

surveys = database_as_array()
to_be_deleted = 'blabla'
result = ''

for line in surveys:
        if line.find(to_be_deleted) != 0:
                result +=(line + '\n')
result = result.split('\n')
result.pop()
print(result)

file = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv', 'w')
i=0
while i < (len(result)-1):
        file.write(result[i] + '\n')
        i += 1
file.close()

# writer = csv.writer(open (r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\TEST\database.csv', 'w'), delimiter=',', escapechar='\n', quoting=csv.QUOTE_NONE)
# for line in result :
#         writer.writerow ([line])


        #     list = self.__dict__
        #     with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\database.csv', 'a', newline='') as file:
        #             writer = csv.DictWriter(file, fieldnames=fields_name)
        #             writer.writerow(list)
# surveys = surveys.pop(       )
# new_clients_database = clients.replace('\n'+ client_to_remove,'')
# new_clients_database = new_clients_database.split('\n')
# new_clients_database.sort
# writer = csv.writer(open ('clientsdb.csv', 'w'), delimiter=',', lineterminator='\n')
# for line in new_clients_database :
# writer.writerow ([line])
# PROBLEM, NEW EMPTY LINE IS ALWAYS CREATED
