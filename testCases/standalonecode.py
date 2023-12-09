import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()
driver.get("https://admin-demo.nopcommerce.com/admin/")
driver.find_element(By.XPATH,"//input[@id='Email']").clear()
driver.find_element(By.XPATH,"//input[@id='Email']").send_keys('admin@yourstore.com')
driver.find_element(By.XPATH,"//input[@id='Password']").clear()
driver.find_element(By.XPATH,"//input[@id='Password']").send_keys('admin')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)


