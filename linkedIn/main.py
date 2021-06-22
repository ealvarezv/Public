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

    # import lxml.html
    #
    # mysite = urllib.request.urlopen('http://www.google.com').read()
    # lxml_mysite = lxml.html.fromstring(mysite)
    #
    # description = lxml_mysite.xpath("//meta[@name='description']") # meta tag description
    # text = description[0].get('content') # content attribute of the tag
    # print(text)
    #








    # url = "https://www.linkedin.com/sales/ssi"
    # response = urllib.request.urlopen(url)
    # print(response.read())

    driver = webdriver.Chrome('C:/Users/ealvarezv/Downloads/chromedriver_win32/chromedriver.exe')
    driver.get('https://www.linkedin.com/login')
    print('Open Web')
    driver.maximize_window()
    # html_source = driver.page_source

    driver.implicitly_wait(5)
    # # driver.get_screenshot_as_file('./screenshot.png')
    username = driver.find_element_by_xpath("//*[@id='username']")
    username.send_keys('enrique.alvarez.villace@gmail.com')
    print('User sent')

    password = driver.find_element_by_xpath("//*[@id='password']")
    password.send_keys('qRg1GzcPF2bk')
    print('Pass sent')

    login = driver.find_element_by_xpath('//*[@type="submit"]')
    login.click()
    print('login')

    driver.get('https://www.linkedin.com/sales/ssi')
    html2 = driver.execute_script("return document.documentElement.innerHTML;")

    print(html2)
    time.sleep(50)

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
