from credentials import username , password
from instapy import InstaPy,smart_run
import os
import time
import random
import spintax
import requests
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from credentials import username as usr, password as passw
from webdriver_manager.firefox import GeckoDriverManager as GM
from itertools import islice


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        user_agent = "Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16"
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", user_agent)
        self.bot = webdriver.Firefox(profile, executable_path=GM().install())
        self.bot.set_window_size(1000, 2000)
        self.followers = []        
        with open(r'urls.txt', 'r') as f:
            urls_lines = [line.strip() for line in f]
        self.urls = urls_lines

    def exit(self):
        bot = self.bot
        bot.quit()

    def login(self):
        bot = self.bot
        bot.get('https://instagram.com/')
        time.sleep(3)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/div[3]/button[1]').click()
        time.sleep(random.uniform(1, 2)*random.uniform(1, 2))

        if check_exists_by_xpath(bot, "//button[text()='Accept']"):
            print("No cookies")
        else:
            bot.find_element_by_xpath("//button[text()='Accept']").click()
            print("Accepted cookies")

        time.sleep(random.uniform(1, 2)*random.uniform(1, 2))
        print("Logging in...")
        time.sleep(5)
        username_field = bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[3]/div/label/input')
        username_field.send_keys(self.username)

        find_pass_field = (By.XPATH, '/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[4]/div/label/input')
        WebDriverWait(bot, 50).until(EC.presence_of_element_located(find_pass_field))
        pass_field = bot.find_element(*find_pass_field)
        WebDriverWait(bot, 50).until(EC.element_to_be_clickable(find_pass_field))
        pass_field.send_keys(self.password)
        bot.find_element_by_xpath('/html/body/div[1]/section/main/article/div/div/div/form/div[1]/div[6]/button').click()
        time.sleep(3)

    def get_posts(self):
        print('Searching post by url...')
        bot = self.bot
        urls = self.urls
        url = urls[0]
        link = url
        bot.get(link)


        number_of_followers_in_comment = 0
        time.sleep(random.uniform(1, 2)*random.uniform(1, 2))
        for mention in self.followers:
            follower_in_list = mention
            comment = " " + follower_in_list
            number_of_followers_in_comment = number_of_followers_in_comment + 1
            if number_of_followers_in_comment == 3:
                number_of_followers_in_comment = 0
                run.comment(comment)
        self.followers = []

    def comment(self, comment):

        bot = self.bot
        print('commenting...')

        bot.execute_script("window.scrollTo(0, window.scrollY + 500)")

        find_comment_box = (By.XPATH, '/html/body/div[1]/section/main/div/div/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        WebDriverWait(bot, 50).until(EC.presence_of_element_located(find_comment_box))
        comment_box = bot.find_element(*find_comment_box)
        WebDriverWait(bot, 50).until(EC.element_to_be_clickable(find_comment_box))
        comment_box.click()
        time.sleep(4+random.uniform(1, 2))
        comment_box.clear()
        comment_box.send_keys(comment + Keys.ENTER)
        time.sleep(4)
    
        # edit this line to make bot faster
        time.sleep(random.uniform(1, 2)*random.uniform(1, 2))
        # ---------------------------------

        # return run.comment(random_comment())



def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return True
    return False


run = Bot(usr, passw)


if __name__ == '__main__':
    while True:
        if run.followers == []:
            nfirstlines = ["pongo mas"]
            n = 10
            with open("followers.txt") as f, open("followerstmp.txt", "w") as out:
                for x in range(n):
                    nfirstlines.append(next(f))
                for line in f:
                    out.write(line)
            os.remove("followers.txt")
            os.rename("followerstmp.txt", "followers.txt")
            run.followers = nfirstlines
        run.login()
        run.get_posts()
        run.exit()
        time.sleep(60*3 +random.uniform(1, 60))
            