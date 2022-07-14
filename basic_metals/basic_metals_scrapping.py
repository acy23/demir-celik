import requests
from bs4 import BeautifulSoup
import csv
from pymongo import MongoClient
from pprint import pprint
import environ
import time
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
                r = requests.get(self.url)
                soup = BeautifulSoup(r.content, 'html5lib')
                #get modified in $oooon
                table = soup.find('td', attrs = {'class':'b'}) 
                print(table)
                self.InsertElements()
            except Exception as err:
                print(err)

                
    def CreateConnector(self):
        myclient = MongoClient(self.host)
        self.client=myclient


    def InsertElements(self,):
        mydb = self.client["testdb"]
        mycol = mydb["TestCollection"]
        mylist=[]
        for i in range(5):
            dt = datetime.now()
            ts = datetime.timestamp(dt)
            mylist.append({ "_id": str(ts), "name": "Yaman", "Roll No": "1001", "Branch":"CSE"})
        x = mycol.insert_many(mylist)

def Main():
    scrapper=ScrapperClass()
    scrapper.CreateConnector()
    scrapper.GatherRespectiveData()
    scrapper.InsertElements()
    
if __name__=="__main__":
    Main()



