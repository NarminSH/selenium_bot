from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
import time

os.environ['username'] = ''
os.environ['password'] = ''
os.environ['person'] = ''


class InstagramBot():
    PATH = ""
    driver = webdriver.Chrome(PATH)

    def __init__(self):
        self.open_site()

    def open_site(self):
        self.driver.get("https://www.instagram.com/")
        self.login()

    def login(self):
        login = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        login.send_keys(os.environ.get('username'))
        login.send_keys(Keys.TAB)
        password = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
        password.send_keys(os.environ.get('password'))
        password.send_keys(Keys.RETURN)
        self.search_person()

    def search_person(self):
        search = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[class='XTCLo x3qfX ']")))
        search.send_keys(os.environ.get('person'))
        self.goto_choosen_profile()

    def goto_choosen_profile(self):
        choosen_profile = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "-qQT3")))
        choosen_profile.send_keys(Keys.ENTER)

        first_pic=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "_9AhH0")))
        first_pic.click()
        time.sleep(2)

        self.like_picture()
    
    def like_picture(self):
        like = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "fr66n")))
        like.click()
        self.next_picture()
    
    def next_picture(self):
        time.sleep(2)
        next = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "coreSpriteRightPaginationArrow")))
        next.click()
        if next:
            self.like_picture()


InstagramBot()