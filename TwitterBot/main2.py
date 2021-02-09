import time
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys

class TwitterBot():
    def __init__(self,username,password):
        self.browser=webdriver.Chrome(r"C:\Users\HknMz\Desktop\github\genel\chromedriver_win32\chromedriver.exe")
        self.username=username
        self.password=password

    def signIn(self):
        self.browser.get("https://www.twitter.com/login")
        time.sleep(5)
        usernameInput=self.browser.find_element_by_name("session[username_or_email]")
        passwordInput=self.browser.find_element_by_name("session[password]")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(5)

    def TweetSomething(self):
        #bot.find_element_by_xpath("//a[@data-testid='AccountSwitcher_Logout_Button']").click()
        tweet = self.browser.find_element_by_xpath('''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div''')
        tweet.send_keys("""Firs Twitter Bot 1""")
        tweet.send_keys(Keys.COMMAND, Keys.ENTER)
        tweet.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span").click()
        time.sleep(5)


    def like_tweets(self, cycles=10):
        bot = self.browser 
        for i in range(cycles):
            try:
                bot.find_element_by_xpath("//div[@data-testid='like']").click()
            except common.exceptions.NoSuchElementException:
                time.sleep(3)
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
                time.sleep(3)
                bot.find_element_by_xpath("//div[@data-testid='like']").click()

            time.sleep(1)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)

    def re_tweets(self, cycles=10):
        bot = self.browser 
        for i in range(cycles):
            try:
                bot.find_element_by_xpath("//div[@data-testid='retweet']").click()
            except common.exceptions.NoSuchElementException:
                time.sleep(3)
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
                time.sleep(3)
                bot.find_element_by_xpath("//div[@data-testid='retweet']").click()

            time.sleep(1)
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1.5)') 
            time.sleep(5)

    def scroll(self):
        bot = self.browser 
        for i in range(20):
            time.sleep(3) 
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight/1)')
            time.sleep(3)  
            #bot.find_element_by_xpath("//div[@data-testid='like']").click()
            time.sleep(3)        

    def like(self, number=5):
        bot = self.browser 
        for i in range(number):
            like_buttons = bot.find_elements_by_xpath("//div[@data-testid='like']")
            for i in range(len(like_buttons)):
                like_buttons[i].click()
                time.sleep(1)
                print(len(like_buttons))
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1)')
            time.sleep(2)

    def unlike(self, number=50):
        bot = self.browser.get("https://www.twitter.com/nag122nag/likes")
        for i in range(number):
            like_buttons = bot.find_elements_by_xpath("//div[@data-testid='unlike']")
            for i in range(len(like_buttons)):
                like_buttons[i].click()
                time.sleep(1)
                print(len(like_buttons))
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight/1)')
            time.sleep(2)


if __name__=="__main__":
    username= input("Enter your username: ")
    password= input("Enter your password: ")
    t=TwitterBot(username,password)
    t.signIn()
    #t.TweetSomething()
    #t.like_tweets()
    #t.re_tweets()
    #t.scroll()
    #t.like()
    t.unlike()
