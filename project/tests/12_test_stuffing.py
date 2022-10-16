from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]/span").click()

assert driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]/ul[3]/a[1]/p').text == 'Мясо бессмертных моллюсков Protostomia'

driver.quit()