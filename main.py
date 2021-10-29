import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "E:\chrome-driver\chromedriver.exe"


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0
        self.go_button = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        self.go_button.click()
        time.sleep(45)
        self.down = self.driver.find_element_by_class_name("download-speed")
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
        down_speed = float(self.down.text)
        up_speed = float(self.up.text)
        print(down_speed)
        print(up_speed)
        self.tweet_at_provider(down_speed, up_speed)

    def tweet_at_provider(self, down, up):
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        username = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        username.send_keys("@twitest0642")
        password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys("testmail123")
        password.send_keys(Keys.ENTER)
        time.sleep(2)
        twitter_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        twitter_input.send_keys(f"Hey @@WLinkComm, why is my internet speed is {down}/{up} while I paid for 100/30.")
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span')
        tweet_button.click()


my_bot = InternetSpeedTwitterBot()
my_bot.get_internet_speed()













