import csv
import flask
from flask import Flask, request, redirect
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


@app.route("/")
def homepage():
    page = get_html("index")
    return page

@app.route('/survey')
def survey():
    page = get_html('survey')
    return page


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
    