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
    # Delete the survey from the CSV when user clicks on button next to the survey in Homepage
    @staticmethod
    def delete_from_CSV(survey_to_remove):
            surveys = database_as_array()
            result = ''
            for line in surveys:
                    if line.find(survey_to_remove) != 0:
                            result +=(line + '\n')
            result = result.split('\n')
            result.pop()
            print(result)
            file = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\database.csv', 'w')
            i=0
            while i < (len(result)-1):
                    file.write(result[i] + '\n')
                    i += 1
            file.close()


# Function to get the clients database as Array
# The aim is to have a dynamic HTML for a dropdown selection for each clients from the database
# Used in @app.route("/survey")
def read_clients_db():
    document = open("clientsdb.csv")
    content = document.read()
    document.close()
    content = content.split('\n')
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
                    surveys += '<td>' + value + ' <button type="submit" name="survey-to-remove" value="' + survey_id + '">Remove</button></td>'
                if col_count == len(column):
                    surveys += '<td>'+ value + '</td></tr>'
                if 3 < col_count < len(column):
                    surveys += '<td>' + value+ '</td>'
                col_count +=1
        line_count +=1

    page = page.replace('$$$ALLSURVEYS$$$',surveys)
    return page

# Delete the survey from the database when user clicks on the remove button
# next to the client's name
@app.route('/', methods=['POST'])
def survey_remove():
    survey_to_remove = request.form['survey-to-remove']
    Shop.delete_from_CSV(survey_to_remove)
    return redirect ('/')

@app.route('/survey')
def survey():
    page = get_html('survey')
    clients_array = read_clients_db()

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

# Page with all the clients from the clientsdb.csv
# a button is created for each client to delete the client
@app.route('/clients')
def clients_page():
    page = get_html('clients')
    clients_array = read_clients_db()
    result=''
    if clients_array[-1] =='':
        clients_array.pop()
    for client in clients_array:
        result += '<li>'+ client + ' <button type="submit" value="' + client+'" name="client-to-remove">Remove</button></li>'
    dynamic_html = page.replace("$$$CLIENTS$$$", result)
    return dynamic_html

# delete the desired client from the database after button click, or add a client
@app.route('/clients', methods=['POST'])
def clients_management_page():
    # To add a client to the database
    if 'client-to-add' in request.form:
        client_to_add = request.form['client-to-add']
        clients = read_clients_db()
        if clients[-1] =='':
            clients.pop()
        clients.append(client_to_add)
        clients.sort()
        file = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\clientsdb.csv', 'w')
        i=0
        while i < (len(clients)):
                file.write(clients[i] + '\n')
                i += 1
        file.close()
    # To remove a client from the database
    elif 'client-to-remove' in request.form:
        client_to_remove = request.form['client-to-remove']
        clients = read_clients_db()
        if clients[-1] =='':
            clients.pop()
        clients.pop((clients.index(client_to_remove)))
        print(clients)
        file = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\clientsdb.csv', 'w')
        i=0
        while i < (len(clients)):
                file.write(clients[i] + '\n')
                i += 1
        file.close()
    return redirect ('/clients')

# TODO add somewhere something to check the CSV exists with the right header, otherwise create it
# TODO survey
# TODO JS pour localStorage
# TODO CSS