from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/ezen_tensorflow/PythonApplication1/PythonApplication1/chromedriver_win32/chromedriver")
driver.get("https://www.google.co.kr/")
# id로 태그 검색하기
search_bar = driver.find_element_by_css_selector("input[title='검색']")
# data 값 삽입
search_bar.send_keys('스크래핑 대상')
# data 값 삽입
search_bar.submit()
sleep(10)

soup = BeautifulSoup(driver.page_source,'html.parser')
print(soup.prettify)
driver.close()