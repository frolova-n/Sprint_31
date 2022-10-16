from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").click()

driver.find_element(By.NAME, "name").send_keys("nataliafrolova3678@ya.ru")

driver.find_element(By.NAME, "Пароль").send_keys("000018")

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button").click()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]/span").click()

time.sleep(3)

assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[1]/p").text == 'Соус Spicy-X'

driver.quit()