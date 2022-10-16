from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a").click()

driver.find_element(By.XPATH, "/html/body/div/div/main/div/div/p[1]/a").click()

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys("Наталья")

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys("nataliafrolov32435@ya.ru")

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys("00001")

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

time.sleep(5)

assert driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p").text == 'Некорректный пароль'

driver.quit()