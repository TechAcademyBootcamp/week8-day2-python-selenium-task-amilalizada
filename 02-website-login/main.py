from selenium import webdriver
from time import sleep 
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get('http://35.225.243.133/admin/login/')
sleep(2)
name=driver.find_element_by_css_selector('#id_username')
name.send_keys('student')
password=driver.find_element_by_css_selector('#id_password')
password.send_keys('qatester')
login=driver.find_element_by_css_selector('#login-form > div.submit-row > input[type=submit]')
login.click()
sleep(2)
driver.close()