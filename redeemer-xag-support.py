import datetime
import pprint
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from random import randint, uniform, shuffle, choice
from selenium_stealth import stealth
import re
import random
import string
import os
import requests
import platform
import asyncio
import base64
import json
import random
from typing import Dict, Any
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import aiohttp
import requests
from colorama import Fore, Back, Style
# haha funny i dont know how to import only necessary modules so here's a 27 line import for no reason LMFAO
clear = lambda: os.system('cls')
# Set the path to the Chrome driver executable
driver_path = 'C:/chromedriver-win64/chromedriver.exe'

cService = webdriver.ChromeService(executable_path='C:/chromedriver-win64/chromedriver.exe')
service = Service('C:\Program Files\Chrome Driver\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--lang=en')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("useAutomationExtension", False) 
driver = webdriver.Chrome(service=cService, options=options)

webhook_url = ''
token = "XAG_KEY"

print(Fore.RED + r"""
 ____  __   __ _   _   ____ __        __   _     ____   _____ 
/ ___| \ \ / /| \ | | / ___|\ \      / /  / \   |  _ \ | ____|
\___ \  \ V / |  \| || |     \ \ /\ / /  / _ \  | |_) ||  _|  
 ___) |  | |  | |\  || |___   \ V  V /  / ___ \ |  _ < | |___ 
|____/   |_|  |_| \_| \____|   \_/\_/  /_/   \_\|_| \_\|_____|
                                                               
    """)
print(Style.RESET_ALL)
print(Fore.GREEN + "I do not fucking know how to python")
print(Fore.GREEN + " ")
print(Fore.GREEN + " ")
print(Fore.LIGHTCYAN_EX + "[XGPC Redeemer]")
print(Style.RESET_ALL) 
def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()
    
def Type_Me(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        sleep(uniform(.08, .12))
wait = WebDriverWait(driver, 1000)

def generateAccount():
    
    # Check for stock
    url = "https://start-pasting.today/api/stock"
    response = requests.get(url)
    data = response.json()
    normal_accounts = data["normal_accounts"]
    print(str(normal_accounts) + " accounts in XAG")
    # Check for balance
    url = "https://start-pasting.today/api/coins"
    headers = {
    "api-token": token
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    balance = data["coins"]
    print(str(balance) + " balance")
    # Generate an account
    url = "https://start-pasting.today/api/generate?type=xbox"
    response = requests.post(url, headers=headers)
    data = response.json()
    account = data["account"]
    global emailid
    global passwordid
    emailid = account["email"]
    passwordid = account["password"]
    username = account["username"]
    print("fetched from XAG "+ emailid + ":" + passwordid + " | -4" + " | New balance: " + str(balance - 4))
    url = "https://xbox.com/en-US/auth/msa?action=logIn"
    driver.get(url)
    
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="loginfmt"]'))) 
    Type_Me(element, emailid)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="passwd"]'))) 
    Type_Me(element, passwordid)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="declineButton"]')))
    element.click()
    # Manual gamertag creation because api did not let me lmfao
    if username == "unset":    
        WebDriverWait(driver, 600000).until(EC.title_contains('Welcome to Xbox'))
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-1"]')))
        button.click()
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
        button.click()

        wait.until(EC.title_contains('Consent'))
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
        button.click()
    sleep(4)


start = input("Type 'start' to begin checking codes: ")
if start == 'start':
        generateAccount()
        
                    
        # List of codes to check
        codes = []
        with open('codes.txt', 'r') as file:
            for line in file:
                code = line.strip()
                codes.append(code)
        valid_count = 0
        invalid_count = 0

        for code in codes:
            
            url = f'https://www.xbox.com/en-US/xbox-game-pass/invite-your-friends/redeem?offerId={code}' 
           
            driver.get(url)
           
            sleep(4)
            page_source2 = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', driver.page_source)
            

            if 'Redeem your 14-day trial, then install the Xbox app to start playing.' in str(page_source2):
                print(f'Code {code} is eligible')
               
                valid_count += 1
                redeem_button = driver.find_element(By.XPATH, "//button[text()='REDEEM NOW']")
                redeem_button.click()
                sleep(3)
                WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME ,'redeem-sdk-hosted-iframe')))
                element = driver.find_element(By.XPATH, "//button[text()='Get Started! Add a way to pay.']")
                element.click()
                WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.ID, 'displayId_credit_card_visa_amex_mc_discover')))
                credit_card = driver.find_element(By.ID,"displayId_credit_card_visa_amex_mc_discover")
                credit_card.click()

                WebDriverWait(driver, 2000).until(EC.presence_of_element_located((By.ID, 'accountToken')))
                account_token = driver.find_element(By.ID,"accountToken")
                account_token.click()
                def get_random_cc_info():
                    with open('ccs.txt', 'r') as file:
                        lines = file.readlines()
                        random_line = random.choice(lines)
                        cc_info = random_line.split("|")
                        cc_date1 = cc_info[1]
                        cc_date2 = cc_info[2]
                        cc_cvv = cc_info[3]
                    return cc_info, cc_date1, cc_date2, cc_cvv
                def do_payment():
                 cc_info, cc_date1, cc_date2, cc_cvv = get_random_cc_info()
                 account_token.send_keys(cc_info[0])
                 name = driver.find_element(By.ID,"accountHolderName")
                 name.click()
                 name.send_keys('Alex')
                 expiry_month = driver.find_element(By.ID, "input_expiryMonth")
                 
                 expiry_month.send_keys(cc_date1)

                 expiry_year = driver.find_element(By.ID, "input_expiryYear")
                 expiry_year.send_keys('27')

                 cvv = driver.find_element(By.ID,"cvvToken")
                 cvv.click()
                 cvv.send_keys(cc_cvv)
                 address_line1 = driver.find_element(By.ID,"address_line1")
                 address_line1.click()
                 address_line1.send_keys('9027 Fairground Circle')

                 address_line2 = driver.find_element(By.ID,"city")
                 address_line2.click()
                 address_line2.send_keys('Oceanside')
                
                 region = driver.find_element(By.ID,"input_region")
                
                 region.send_keys('New York')

                 postal = driver.find_element(By.ID,"postal_code")
                 postal.click()
                 postal.send_keys('11572')

                 save1 = driver.find_element(By.ID,"pidlddc-button-saveButton")
                 save1.click()
                 WebDriverWait(driver, 5000).until(EC.presence_of_element_located((By.CLASS_NAME, "lightweight--_B359BGN.base--goua8jma")))
                try:
                    get_random_cc_info()
                    do_payment()
                except:
                    get_random_cc_info()
                    do_payment()
                sleep(3)
                txt = driver.find_element(By.CLASS_NAME, 'lightweight--_B359BGN.base--goua8jma')
                txt.click()

                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pidlddc-text-profileAddressPageSubheading')))
                WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, 'pidlddc-text-profileAddressPageSubheading')))
               
                address_line1 = driver.find_element(By.ID,"address_line1")
                address_line1.click()
                address_line1.send_keys('9027 Fairground Circle')

                address_line2 = driver.find_element(By.ID,"city")
                address_line2.click()
                address_line2.send_keys('Oceanside')
                
                region = driver.find_element(By.ID,"input_region")
                
                region.send_keys('New York')

                postal = driver.find_element(By.ID,"postal_code")
                postal.click()
                postal.send_keys('11572')
                save1 = driver.find_element(By.ID,"pidlddc-button-saveButton")
                save1.click()
                WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pidlddc-button-addressUseButton')))


                sleep(1)
                save2 = driver.find_element(By.ID,"pidlddc-button-addressUseButton")
                save2.click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "primary--kLopxQTl.base--goua8jma")))
                sleep(1)
                cbf = driver.find_element(By.CLASS_NAME, 'primary--kLopxQTl.base--goua8jma')
                cbf.click()
                sleep(23)

                

                
                global current_day
                global current_month
                current_day = datetime.datetime.now().day
                current_month = datetime.datetime.now().strftime("%b")
                print(Fore.GREEN + '+ Redeemed ' + emailid + '@outlook.com:' + passwordid + ' | ' + str(current_month) + ' ' + str(current_day))
                print(Style.RESET_ALL)
                sleep(2)
                driver.get('https://www.xbox.com/en-US/auth/msa?action=logOut')
                sleep(3)
                driver.delete_all_cookies()
                sleep(1)
                generateAccount()
                # pls god strike this nigga down
                
           
                

                
            

driver.quit()
print(Fore.GREEN + '+ end | ' + str(valid_count))
print(Style.RESET_ALL)


