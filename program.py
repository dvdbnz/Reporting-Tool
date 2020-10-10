import csv
import flask
from flask import request, redirect
from datetime import datetime

app = flask.Flask("Reporting Tool")

# Get the HTML content
def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

#function to get database as array
def database_as_array():
    database = open("database.csv")
    survey = database.read()
    database.close()
    survey = survey.split("\n")
    return survey

# creation of the Shop class
class Shop:
    def __init__ (self, client, lg_oled, sony_oled):
        self.datetime = datetime.now().strftime('%d.%m.%y %H:%M:%S')
        self.client = client
        self.lg_oled = lg_oled
        self.sony_oled = sony_oled
        self.id = str(self.datetime) + '_' + client
    # Convert object as dict to add it to the csv
    def add_new_line_to_csv(self):
            fields_name = ['id', 'datetime', 'client','lg_oled','sony_oled']
            list = self.__dict__
            with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\database.csv', 'a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fields_name)
                    writer.writerow(list)
    # @staticmethod
    # def delete_from_CSV():


# Function to get the clients database as Array
# The aim is to have a dynamic HTML for a dropdown selection for each clients from the database
# Used in @app.route("/survey")
def read_clients_db():
    document = open("clientsdb.csv")
    content = document.read()
    document.close()
    # clients_array = content.split('\n')
    return content



                                                        # SERVER

@app.route("/")
def homepage():
    page = get_html("index")

    # To display the list of all the surveys in a table 
    list_of_surveys = database_as_array()
    if list_of_surveys[-1] =='': #Check if the last line is empty, and if yes, pop last value
        list_of_surveys.pop()
    surveys = ''
    line_count=1

    # Parse CSV to create HTML as a table
    for line in list_of_surveys:
        # If it is the header
        if line_count == 1:
            column = line.split(',')
            col_count=1
            for value in column:
                if col_count == 2:
                    surveys += '<tr><th>'+value+'</th>'
                if col_count == len(column):
                    surveys += '<th>'+value+'</th></tr>'
                if 2 < col_count < len(column):
                    surveys += '<th>'+value+'</th>'
                col_count += 1  
        # For other lines of the csv
        else:
            column = line.split(',')
            col_count = 1
            survey_id=''
            for value in column:
                if col_count == 1:
                    survey_id = str(value)
                if col_count == 2:
                    surveys += '<tr><td>' + value + '</td>'
                if col_count == 3: #button to remove a survey
                    surveys += '<td>' + value + ' <button type="submit" name="client-to-remove" value="' +survey_id + '">''</button></td>'
                if col_count == len(column):
                    surveys += '<td>'+ value + '</td></tr>'
                if 3 < col_count < len(column):
                    surveys += '<td>' + value+ '</td>'
                col_count +=1
        line_count +=1

    page = page.replace('$$$ALLSURVEYS$$$',surveys)
    return page

@app.route('/survey')
def survey():
    page = get_html('survey')
    clients = read_clients_db()
    clients_array = clients.split('\n')

    # Format a HTML dropdown selection for each clients from the database
    result = ''
    clients_array.pop()
    for client in clients_array:
        result += '<option value="' + client + '">'+client+'</option>'
    dynamic_html = page.replace("$$$OPTIONS$$$", result)

    return dynamic_html

#When the user clicks on submit the data from the survey, it gets the values from the survey.html
#Then uses them as arguments to create an object. Then append the object as Dict in the Csv
# Then redirect to the homepage
@app.route('/survey', methods=['POST'])
def survey_request():
    client = request.form['client']
    lg_oled = request.form['lg-oled']
    sony_oled = request.form['sony-oled']
    NewClient = Shop(client,lg_oled,sony_oled)
    NewClient.add_new_line_to_csv()
    return redirect('/')

@app.route('/clients')
def clients_page():
    page = get_html('clients')
    return page


@app.route('/clients', methods=['POST'])
def clients_remove():
    client_to_remove = request.form['client-to-remove']
    clients = read_clients_db()
    new_clients_database = clients.replace('\n'+ client_to_remove,'')
    new_clients_database = new_clients_database.split('\n')
    new_clients_database.sort
    writer = csv.writer(open ('clientsdb.csv', 'w'), delimiter=',', lineterminator='\n')
    for line in new_clients_database :
        writer.writerow ([line])
        # PROBLEM, NEW EMPTY LINE IS ALWAYS CREATED
    return redirect('/')

# TODO add somewhere something to check the CSV exists with the right header, otherwise create it
# TODO faire un bouton pour ajouter un client à la base de donnée.
# TODO survey
# TODO JS pour localStorage
# TODO CSS