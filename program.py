import csv
import flask
from flask import request, redirect
import cgi
from datetime import datetime

app = flask.Flask("Reporting Tool")

def get_html(page_name):
    html_file = open(page_name + ".html")
    content = html_file.read()
    html_file.close()
    return content

# creation of the Shop class
class Shop:
    def __init__ (self, client, lg_oled, sony_oled):
        self.datetime = datetime.now().strftime('%d.%m.%y %H:%M:%S')
        self.client = client
        self.lg_oled = lg_oled
        self.sony_oled = sony_oled
    # Convert object as dict to add it to the csv
    def add_new_line_to_csv(self):
            fields_name = ['datetime', 'client','lg_oled','sony_oled']
            list = self.__dict__
            with open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\database.csv', 'a', newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fields_name)
                    writer.writerow(list)
            print(list)


# Function to get the clients database as Array
# The aim is to have a dynamic HTML for a dropdown selection for each clients from the database
def read_clients_db():
    document = open("clientsdb.csv")
    content = document.read()
    document.close()
    clients_array = content.split('\n')
    return clients_array

@app.route("/")
def homepage():
    page = get_html("index")
    return page

@app.route('/survey')
def survey():
    page = get_html('survey')
    clients_array = read_clients_db()

    # Format a HTML dropdown selection for each clients from the database
    result = ''
    for client in clients_array:
        result += '<option value="' + client + '">'+client+'</option>'
    dynamic_html = page.replace("$$$OPTIONS$$$", result)

    return dynamic_html

#When the user clicks on submit the data from the survey, it gets the values from the survey.html
#Then uses them as arguments to create an object. Then append the object as Dict in the Csv
# Then redirect to the homepage
@app.route('/survey', methods=['POST'])
def my_form_post():
    client = request.form['client']
    lg_oled = request.form['lg-oled']
    sony_oled = request.form['sony-oled']
    NewClient = Shop(client,lg_oled,sony_oled)
    NewClient.add_new_line_to_csv()
    return redirect('/')


# TODO faire un bouton pour ajouter un client à la base de donnée.
# TODO survey
# TODO JS pour localuser
