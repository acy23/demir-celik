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
        client_mongo = MongoClient(self.host)
        db=client_mongo.admin
        serverStatusResult=db.command("serverStatus")
        pprint(serverStatusResult)
        self.client=client_mongo


def Main():
    scrapper=ScrapperClass()
    scrapper.CreateConnector()
    


if __name__=="__main__":
    Main()



