import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
from pprint import pprint
import environ
import time
import os
import dryscrape
from urllib.request import Request, urlopen
from urllib import parse
from datetime import datetime

class ScrapperClass():

    def __init__(self):
        env = environ.Env()
        environ.Env.read_env()
        self.host=env('HOST')
        self.url="https://www.metalsdaily.com/live-prices/"

    def GatherRespectiveData(self):
        while True:
            try:
                session = dryscrape.Session()
                session.visit(self.url)
                response = session.body()
                soup = BeautifulSoup(response)
                soup.find('td', attrs={"class" : "b"})
                break
                #self.InsertElements()
            except Exception as err:
                print(err)
                #<span class="data-table-row-cell__value">2,951.00</span>

    def CreateConnector(self):
        myclient = MongoClient(self.host)
        self.client=myclient


    def InsertElements(self):
        mydb = self.client["testdb"]
        mycol = mydb["service1_api_basic_metals"]
        mylist=[]
        dic={   
                "id": 10,
                "category": "Yaman",
                "price": 1001,
                "parity":"CSE"
                }
        for i in range(20,30):
            #dt = datetime.now()
            #ts = datetime.timestamp(dt)
            mylist.append(
                {
                "id": i,
                "category": "Yaman Sener",
                "price": 1001,
                "parity":"CSE"
                }
            )
        x = mycol.insert_many(mylist)

def Main():
    scrapper=ScrapperClass()
    scrapper.CreateConnector()
    scrapper.GatherRespectiveData()
    #scrapper.InsertElements()
    
if __name__=="__main__":
    Main()



