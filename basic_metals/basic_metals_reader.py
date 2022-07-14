import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
from pprint import pprint
import environ


class ReaderClient():

    def __init__(self):
        env = environ.Env()
        environ.Env.read_env()
        self.host=env('HOST')
    
    def CreateConnector(self):
        myclient = MongoClient(self.host)
        self.client=myclient

    def ReadDb(self):
        mydb = self.client["testdb"]
        mycol = mydb["TestCollection"]
        myquery = { "name": "John" }
        mydoc = mycol.find(myquery)
        return mydoc

def Main():
    reader_client=ReaderClient()
    reader_client.CreateConnector()
    reader_client.ReadDb()

Main()