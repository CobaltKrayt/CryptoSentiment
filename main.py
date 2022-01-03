import csv
from getpass import getpass
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

wait = WebDriverWait(driver, 30)
driver.get("https://www.twitter.com/login")

username = wait.until(EC.visibility_of_element_located((By.NAME, "text")))
username.send_keys('George Covalciuc')