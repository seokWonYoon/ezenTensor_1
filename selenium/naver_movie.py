from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/ezen_tensorflow/PythonApplication1/PythonApplication1/chromedriver_win32/chromedriver")
driver.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")

soup = BeautifulSoup(driver.page_source,'html.parser')
#print(soup.prettify)
all_div = soup.find_all('div', {'class':'tit3'})
for i in [div.a.string for div in all_div]:
    print(i)
driver.close()