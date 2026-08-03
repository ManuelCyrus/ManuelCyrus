from selenium import webdriver
import time


for i in range(1200):
    driver = webdriver.Chrome()

    driver.get("google")

    driver.quit()  # Fecha o navegador completamente