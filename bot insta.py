# first of all, to run this bot, you need to install Selenium (try: pip install selenium)
# after that, you must have firefox browser installed in your pc
# then, install firefox webdriver (Gecko Driver) -> https://github.com/mozilla/geckodriver/releases

from selenium import webdriver
from time import sleep

username = ""  # inside the quotation marks you need to write your username
password = ""  # here you write you password
comment = ""  # last but not least, inside this quotation marks you should write the content of your comment

# bellow here, insert the path way to the Gecko driver that you had install, including .exe file
driver = webdriver.Firefox(executable_path=r'path\to\your\geckodriver.exe')
driver.implicitly_wait(5)  # waiting 5 seconds to load

def initialingTheBrowser():
    driver.get('https: put here the instagram post link')  # link of the post ypu want to interact
    sleep(5)  # waiting 5 seconds to load the page
    login()

def login():
    # after successfully loading the web page, the bot will start login in
    driver.find_element_by_css_selector('button.L3NKy').click()
    driver.find_element_by_css_selector("input[name='username']").send_keys(username)
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    driver.find_element_by_css_selector('div.Igw0E:nth-child(4) > button:nth-child(1)').click()
    sleep(5)  # waiting 5 seconds to load the page
    commenting()

def commenting():
    # after successfully login in, the bot will start commenting, infinite loop, to stop, just close the page to stop
    while True:
        driver.find_element_by_css_selector('._15y0l > button:nth-child(1)').click()
        driver.find_element_by_css_selector('.Ypffh').send_keys(comment)
        driver.find_element_by_css_selector('.y3zKF').click()
        sleep(15)  # breaks of 15 seconds between a comment and another one

""""if you want to automatically close the page after N numbers of comments, you can just start a FOR LOOP in range(N):
after insert the code above (the one inside of the while, responsible to comment) and then, outside the FOR LOOP, add:
driver.close()"""
