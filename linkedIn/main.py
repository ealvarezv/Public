# $language = "python"
# $interface = "1.0"

# Main function of the script

# ################### IMPORT ####################
import json
import os
import time
import smtplib
import urllib.request
import requests

from bs4 import BeautifulSoup
from selenium import webdriver


# ################### CONSTANTS ####################
OUTPUT_FOLDER = "_output/"


# ################### FUNCTIONS ####################
# Function to know the status of each locator
def getData():
    # url = "https://www.linkedin.com/sales/ssi"
    # response = urllib.request.urlopen(url)
    # print(response.read())

    driver = webdriver.Chrome('C:/Users/ealvarezv/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.linkedin.com/sales/ssi')
    print('Open Web')
    driver.maximize_window()
    html_source = driver.page_source

    driver.implicitly_wait(5)
    print(html_source)
    driver.get_screenshot_as_file('/screenshot.png') 
    username = driver.find_element_by_id('username')
    username.send_keys('enrique.alvarez.villace@gmail.com')
    print('User sent')
    # time.sleep(1)
#     password = driver.find_element_by_class_name('session_password')
#     password.send_keys('password')
#     print('Pass  sent')
#     time.sleep(1)
#     login = driver.find_element_by_class_name('login-submit')
#
# # log_in_button = driver.find_element_by_class_id('login submit-button')
#
# # locate submit button by_xpath
# # log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
#
#     login.click()
#     print('login')
#
#     time.sleep(100)
    # linkedin_urls = driver.find_elements_by_class_name('iUh30')

    # url = "https://www.linkedin.com/sales/ssi"
    # response = requests.get(url).text
    # soup = BeautifulSoup(response, "lxml")
    # print(soup.prettify())
    #
    # mylink = soup.find("find-people__sub-score-bar")
    # print(mylink)

# Main Function
def main():
    print("\n#################### START ####################")

    # currentFolder = os.path.dirname(os.path.abspath(__file__))
    # fileName = (currentFolder + "/" + OUTPUT_FOLDER + "confinamiento.txt")
    # objFile = open(fileName, "a")

    getData()

    print("\n#################### GAME OVER ####################\n")


# ################### EJECUCIÓN ####################
# Script execution
main()
