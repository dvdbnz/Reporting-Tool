import csv
import flask
from flask import request, redirect
from datetime import datetime

def database_as_array():
    database = open(r'C:\Users\davbu\OneDrive\Dokumente\Learning\TCC\Final Project\database.csv')
    survey = database.read()
    database.close()
    survey = survey.split("\n")
    return survey

list_of_surveys = database_as_array()
surveys = ''
line_count=1

