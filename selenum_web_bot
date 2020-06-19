# First of all, to run this bot, you need to install Selenium (try: pip install selenium)
# after that, you must have firefox browser installed in your pc
# then, install firefox webdriver (Gecko Driver) -> https://github.com/mozilla/geckodriver/releases

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

username = input()  # inside the quotation marks you need to write your username
password = input()  # here you write you password 
instagram_link = input() #last but not least, instagram main account link 
#--> i left three of it as an input because its easier to run on the command prompt

# bellow here, insert the path way to the Gecko driver that you had install, including .exe file
driver = webdriver.Firefox(executable_path=r'path\to\your\geckodriver.exe')
driver.implicitly_wait(5)  # waiting 5 seconds to load
#after this, don't need more changes, just run the programm

#bot time to work:

def Following():
    # after successfully login in, the bot will start following all the accounts.


    #cheking if there is any pop-up
    try:
        driver.find_element_by_css_selector('button.sqdOP:nth-child(1)').click()
    except:
        pass

    #extrating the number of followers the main account has
    followers = WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
        (By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"))).get_attribute("title")

    #verifying if the main account has more then 1000 followers, if positive, the bot need to do an string manipulation
    if "." in followers:
        followers = followers.replace(".", "")

    #openning the followers tab
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

    #following all the accounts
    cont = 0
    while cont != int(followers) + 1:
        for x in range(1, int(followers)):
            cont+= 1
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/ul/div/li[{}]/div/div[3]/button'.format(x)).click()
            sleep(2)


def Login(username, password):
    # after successfully loading the web page, the bot will start login in
    driver.find_element_by_css_selector('button.L3NKy').click()
    driver.find_element_by_css_selector("input[name='username']").send_keys(username)
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    driver.find_element_by_css_selector('div.Igw0E:nth-child(4) > button:nth-child(1)').click()
    sleep(5)  # waiting 5 seconds to load the page
    Following()

def InitializingTheBrowser(link):
    driver.get(link)  # link of the post you want to interact
    sleep(5)  # waiting 5 seconds to load the page
    Login(username, password)

if __name__ == '__main__':
    InitializingTheBrowser(instagram_link)
    #initializing the program






