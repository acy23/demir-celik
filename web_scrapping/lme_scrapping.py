import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
from pprint import pprint
import environ

class ScrapperClass():

    def __init__(self):
        env = environ.Env()
        environ.Env.read_env()
        self.host=env('HOST')
        self.url="scrapping_url"

    def GatherRespectiveData():
        URL = ""
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

    def CreateConnector(self):
        myclient = MongoClient(self.host)
        self.client=myclient
    
    def InsertElements(self):
        mydb = self.client["testdb"]
        mycol = mydb["TestCollection"]
        mydict = { "name": "John", "address": "Highway 420" }
        x = mycol.insert_one(mydict)
        print(x)

def Main():
    scrapper=ScrapperClass()
    scrapper.CreateConnector()
    scrapper.InsertElements()
    
if __name__=="__main__":
    Main()



