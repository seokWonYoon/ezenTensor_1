from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("C:/ezen_tensorflow/PythonApplication1/PythonApplication1/chromedriver_win32/chromedriver")
driver.implicitly_wait(3) #lazy loading

driver.get("http://nid.naver.com/nidlogin.login")
driver.find_element_by_name('id').send_keys("elilizerd")
driver.find_element_by_name('pw').send_keys("Dbstjrdnjs0195$")
driver.implicitly_wait(3) #lazy loading

driver.find_element_by_xpath('//$[@id="frmNIDLogin"]/fieldset/input').click()
driver.implicitly_wait(3) #lazy loading

driver.get("https://order.pay.naver.com/home")
html = driver.page_source


soup = BeautifulSoup(driver.page_source,'html.parser')
notice = soup.select('div.p_inr > div.p_info > a > span')

for i in notice:
    print(i.text.strip())

driver.close()