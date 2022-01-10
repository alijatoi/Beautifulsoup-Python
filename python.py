#Python program to scrape website
#and save blog authors info from website https://flyingknowledge.com/
#Importing Libraries 
import requests
from bs4 import BeautifulSoup
import csv
import re


URL = "https://flyingknowledge.com/"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

#Creating List 
quotes=[] # a list to store 

table = soup.find('div', attrs = {'id':'td-outer-wrap'})

names=[]
 
#Find by span tag of the website
for row in table.findAll('span',
						attrs = {'class':'td-post-author-name'}):
	namess=(row.find('a').contents[0])
	names.append(namess.text)    
  
#Writing Data into CSV File
# CSV File Name : OUPT2.csv
with open('OUPT2.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  # Publisher Name is Coloumn Header Text in of CSV File
  writer = csv.DictWriter(csv_1, fieldnames = ["Publisher Name"])
  writer.writeheader()
#Header(coloumn) Text is Written Now writting Data in rows
  csv_out.writerows([names[index]] for index in range(0, len(names)))
