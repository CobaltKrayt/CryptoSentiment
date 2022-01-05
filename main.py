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
username.send_keys('GmanCC')

username.send_keys(Keys.RETURN)

password = wait.until(EC.visibility_of_element_located((By.NAME,"password")))
password.send_keys('Georgia804bot')

password.send_keys(Keys.RETURN)

search = wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@aria-label="Search query"]')))
search.send_keys('#cryptocurrency')
search.send_keys(Keys.RETURN)

cards = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//article[@data-testid="tweet"]')))
card = cards[0]

# username
# ./div/div/div/div[2]/div[2]/div[1]//span

username = card.find_element(By.XPATH,'.//span').text
userTag = card.find_element(By.XPATH,'.//span[contains(text(),"@")]').text
postTime = card.find_element(By.XPATH,'.//time').get_attribute('datetime')
tweetContent = card.find_element(By.XPATH,'./div/div/div/div[2]/div[2]/div[2]/div[1]').text
respondingTo = card.find_element(By.XPATH,'./div/div/div/div[2]/div[2]/div[2]/div[2]').text

replyCount = card.find_element(By.XPATH,'.//div[@data-testid="reply"]').text


print(username)
print(userTag)
print(postTime)
print(tweetContent)
print(respondingTo)
print(replyCount)

