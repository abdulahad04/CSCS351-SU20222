from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

#id and password of your github account goes here
userID = "zen4"
password = "typo"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://github.com/login")


try:
    driver.find_element(By.NAME, 'login').send_keys(userID)
    driver.find_element(By.NAME, 'password').send_keys(password)

    #The path to sign in button
    driver.find_element(By.XPATH, '//*[@id="login"]/div[4]/form/div/input[12]').click()

    title = driver.title
    sleep(10)


    if title =='GitHub':
        print("Login was successful")
    else:
        print("Login unsuccessful")

except:
    print("Login unsuccessful")