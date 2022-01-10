import csv
from getpass import getpass
from time import sleep

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def getTweetData(card):
    try:
        postTime = card.find_element(By.XPATH, './/time').get_attribute('datetime')
    except NoSuchElementException:
        return

    username = card.find_element(By.XPATH, './/span').text
    userHandle = card.find_element(By.XPATH, './/span[contains(text(),"@")]').text
    tweetContent = card.find_element(By.XPATH, './div/div/div/div[2]/div[2]/div[2]/div[1]').text
    respondingTo = card.find_element(By.XPATH, './div/div/div/div[2]/div[2]/div[2]/div[2]').text

    replyCount = card.find_element(By.XPATH, './/div[@data-testid="reply"]').text
    retweetCount = card.find_element(By.XPATH, './/div[@data-testid="retweet"]').text
    likeCount = card.find_element(By.XPATH, './/div[@data-testid="like"]').text

    tweet = (username, userHandle, postTime,tweetContent,respondingTo,replyCount,retweetCount,likeCount)
    return tweet

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

# cards = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//article[@data-testid="tweet"]')))

# username
# ./div/div/div/div[2]/div[2]/div[1]//span
tweetDataList = []
tweetIds = set()
lastPosition = driver.execute_script("return window.pageYOffset;")
scrolling = True

while scrolling:
    pageCards = wait.until(EC.visibility_of_all_elements_located((By.XPATH,'//article[@data-testid="tweet"]')))
    for card in pageCards[-15:]:
        tweet = getTweetData(card)
        if tweet:
            currentTweetId = ''.join(tweet)
            if currentTweetId not in tweetIds:
                tweetIds.add(currentTweetId)
                tweetDataList.append(tweet)

    scrollAttempt = 0
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
        sleep(1)
        currentPosition = driver.execute_script("return window.pageYOffset;")
        if lastPosition == currentPosition:
            scrollAttempt += 1

            if scrollAttempt >= 3:
                scrolling = False
                break
            else:
                sleep(2)
        else:
            lastPosition = currentPosition
            break

df = pd.DataFrame(tweetDataList)
df.to_csv('tweetData.csv',header=['Username','Handle','Timestamp','CommentCount', 'Likes','Retweets', 'Text'],encoding='utf-8', index=False)



