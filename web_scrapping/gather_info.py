from re import S
import requests
from bs4 import BeautifulSoup
import csv


class ScrapperClass():

    def __init__(self):
        pass
    def GatherRespectiveData():
        URL = ""
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')

    def CreateConnector(self):
        

def Main():
    pass
print(1)


if __name__=="__main__":
    Main()