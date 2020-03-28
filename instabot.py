from selenium import webdriver
from time import sleep

class InstaBot:
    def __init__(self, username, pwd):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(username)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pwd)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        
InstaBot('username', 'password')



