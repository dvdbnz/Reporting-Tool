import csv
import flask
app = flask.Flask("Reporting Tool")

class Shop:
    def __init__ (self, name, tv_a, tv_b, tv_c):
        self.name = name
        self.tv_a = tv_a
        self.tv_b = tv_b
        self.tv_c = tv_c

@app.route("/")
def homepage():
    return "HOMEPAGE"