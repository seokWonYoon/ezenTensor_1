from bs4 import BeautifulSoup
import re

def read_file():
    file = open("C:\ezen_tensorflow\PythonApplication1\PythonApplication1\consumer_reports.txt",'rt',encoding='utf-8')
    data=file.read()
    file.close()
    # print(data)
    return data

soup = BeautifulSoup(read_file(),'lxml')
all_div = soup.find_all("div",attrs={'class':'entry-letter'})
products = [div.div.a.span.string for div in all_div]
for i in products:
    print(i)