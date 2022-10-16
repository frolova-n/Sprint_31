from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

time.sleep(3)

assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").text == 'Войти'

driver.quit()