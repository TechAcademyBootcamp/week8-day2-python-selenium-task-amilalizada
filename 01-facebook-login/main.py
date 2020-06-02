from selenium import webdriver
from time import sleep
driver = webdriver.Firefox(executable_path="./geckodriver")
driver.get('https://www.facebook.com')
sleep(2)
email_input=driver.find_element_by_css_selector('#email')
email_input.send_keys('cascasca')
password=driver.find_element_by_css_selector('#pass')
password.send_keys('ascascas')
login=driver.find_element_by_css_selector('#u_0_b')
login.click()
sleep(3)

driver.close()
