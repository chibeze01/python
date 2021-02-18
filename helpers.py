# Dependencies
import requests as req
from bs4 import BeautifulSoup
import csv

class helpers:

    def __init__(self):
        pass

    # class for handling data gathering and sending
    class data:
        # Get the htmldocument of the website
        # param: url
        # return: beautified html document
        def get(url= 'https://tradingeconomics.com', div_class = "table-responsive" ) -> str:
            source = req.get(url).text
            soup = BeautifulSoup(source, 'lxml')
            table = [i.text.strip() for i in
                    soup.find('div', class_=div_class).find_all('a')]
            
            # write data to a csv file
            with open('.data/table/table.csv', 'w', newline='') as csvfile:
                fwriter = csv.writer(csvfile)

                count = 1
                string = 'country'
                for i in table:
                    if count != 10:
                        string += "," + i
                        count +=1
                    else :
                        string =string.strip(',')
                        # write data to a file
                        fwriter.writerow(string.split(','))
                        string =''
                        count = 0
            csvfile.close()

        # def post:
        # def delete:
