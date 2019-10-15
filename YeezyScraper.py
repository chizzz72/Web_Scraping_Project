from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import csv
import re
import time
driver = webdriver.Chrome("C:/Users/kevin/Desktop/chromedriver.exe")

#login

#driver.get('https://stockx.com/login')
#myemail = 'email@.com'
#mypassword = '123456abc'
#email = driver.find_element_by_name("email")
#password = driver.find_element_by_name("password")
#email.send_keys(myemail)
#time.sleep(5)
#password.send_keys(mypassword)
#time.sleep(5)
#Login_button = driver.find_element_by_xpath('//button[@data-testid="product-next-button" and @class="button right-button button-green"]')
#Login_button.click()

#yeezy boost 350, 500, 700 models in 2018, 2019
url_list = ['https://stockx.com/adidas-yeezy-boost-350-v2-citrin', 'https://stockx.com/adidas-yeezy-boost-350-v2-lundmark', 'https://stockx.com/adidas-yeezy-boost-350-v2-sesame',
           'https://stockx.com/adidas-yeezy-boost-350-v2-clay', 'https://stockx.com/adidas-yeezy-boost-350-v2-static', 'https://stockx.com/adidas-yeezy-boost-350-v2-butter', 
           'https://stockx.com/adidas-yeezy-boost-350-v2-glow', 'https://stockx.com/adidas-yeezy-boost-350-v2-synth', 'https://stockx.com/adidas-yeezy-boost-350-v2-true-form', 
           'https://stockx.com/adidas-yeezy-boost-350-v2-antlia', 'https://stockx.com/adidas-yeezy-boost-350-v2-static-black-reflective', 'https://stockx.com/adidas-yeezy-boost-350-v2-static-reflective', 
           'https://stockx.com/adidas-yeezy-boost-350-v2-hyperspace', 'https://stockx.com/adidas-yeezy-boost-350-v2-black', 'https://stockx.com/adidas-yeezy-boost-350-v2-lundmark-reflective',
           'https://stockx.com/adidas-yeezy-boost-350-v2-antlia-reflective', 'https://stockx.com/adidas-yeezy-boost-350-v2-synth-reflective', 'https://stockx.com/adidas-yeezy-boost-500-bone-white',
           'https://stockx.com/adidas-yeezy-500-salt', 'https://stockx.com/adidas-yeezy-500-utility-black', 'https://stockx.com/adidas-yeezy-500-blush', 
           'https://stockx.com/adidas-yeezy-500-desert-rat-moon-yellow', 'https://stockx.com/adidas-yeezy-500-shadow-black-ff', 'https://stockx.com/adidas-yeezy-boost-700-magnet', 
           'https://stockx.com/adidas-yeezy-boost-700-v2-geode', 'https://stockx.com/adidas-yeezy-boost-700-inertia', 'https://stockx.com/adidas-yeezy-boost-700-v2-vanta',
           'https://stockx.com/adidas-yeezy-boost-700-analog', 'https://stockx.com/adidas-yeezy-boost-700-utility-black', 'https://stockx.com/adidas-yeezy-700-mauve', 
           'https://stockx.com/adidas-yeezy-boost-700-salt', 'https://stockx.com/adidas-yeezy-boost-700-v2-tephra', 'https://stockx.com/adidas-yeezy-700-v2-static', 
           'https://stockx.com/adidas-yeezy-boost-700-teal-blue']



csv_file = open('yeezydb.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(['NAME', 'COLORWAY', 'ONEY_SALE', 'RETAIL_PRICE', 'RESELL_PRICE', 'RELEASE_DATE', 'RESELL_DATE', 'SIZE'])

def YeezyScraper():
    time.sleep(3)
    NAME = driver.find_element_by_xpath('//h1[@class="name" and @data-testid="product-name"]').text
    COLORWAY = driver.find_element_by_xpath('//span[@data-testid="product-detail-colorway"]').text
    RETAIL_PRICE = driver.find_element_by_xpath('//span[@data-testid="product-detail-retail price"]').text
    RELEASE_DATE = driver.find_element_by_xpath('//span[@data-testid="product-detail-release date"]').text
    
    parent_element = driver.find_elements_by_xpath('//div[@class="gauges"]')
    for element in parent_element:
        ONEY_SALE = element.find_element_by_xpath('.//div[@class="gauge-container"][1]//div[@class="gauge-value"]').text
    
    #view all sales button
    driver.find_element_by_xpath('//div[@class="last-sale-block"]//a').click()
    time.sleep(3)
    
    history = driver.find_elements_by_xpath('//table[@class="activity-table table table-condensed table-striped "]/tbody//tr')
    for bid in history:
        RESELL_DATE = bid.find_element_by_xpath('./td[1]').text
        SIZE = bid.find_element_by_xpath('./td[3]').text
        RESELL_PRICE = bid.find_element_by_xpath('./td[4]').text
        
        print(NAME, COLORWAY, ONEY_SALE, RETAIL_PRICE, RESELL_PRICE, RELEASE_DATE, RESELL_DATE, SIZE)
        print('-'*50)
        
        
        Yeezy_dict = {}
        Yeezy_dict['NAME'] = NAME
        Yeezy_dict['COLORWAY'] = COLORWAY
        Yeezy_dict['ONEY_SALE'] = ONEY_SALE
        Yeezy_dict['RETAIL_PRICE'] = RETAIL_PRICE
        Yeezy_dict['RESELL_PRICE'] = RESELL_PRICE
        Yeezy_dict['RELEASE_DATE'] = RELEASE_DATE
        Yeezy_dict['RESELL_DATE'] = RESELL_DATE
        Yeezy_dict['SIZE'] = SIZE        
        writer.writerow(Yeezy_dict.values())
        
#        time.sleep(3)
    
try:
    for url in url_list:
#        time.sleep(3)
        driver.get(url)
        time.sleep(3)
        YeezyScraper()
#        time.sleep(3)
except Exception as e:
    print(e)
#    time.sleep(3)
    csv_file.close()
    driver.close()
