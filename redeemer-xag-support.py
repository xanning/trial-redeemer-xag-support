import datetime
import pprint
from time import sleep
from selenium import webdriver # Required
from selenium.webdriver.chrome.options import Options  # Required
from selenium.webdriver.chrome.service import Service  # Required
from selenium.webdriver.common.by import By  # Required
from selenium.webdriver.support.ui import WebDriverWait  # Required
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException # required
from selenium.webdriver.support import expected_conditions as EC # Probably don't need it.
from selenium.webdriver.remote.webelement import WebElement # Probably don't need it.
from random import randint, uniform, shuffle, choice # Required
from urllib.parse import urlparse, parse_qs # Required
# Required
import re
import random
import string
import os
import requests
import json
import random
from typing import Dict, Any # Required
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities # Probably don't need it.
from colorama import Fore, Back, Style # Required
# haha funny i dont know how to import only necessary modules so here's a 27 line import for no reason LMFAO
clear = lambda: os.system('cls')
# Set the path to the Chrome driver executable HERE
driver_path = 'C:/chromedriver-win64/chromedriver.exe'
# Do not change this unless you know what you're doing
sFTTag_url = "https://login.live.com/oauth20_authorize.srf?client_id=00000000402B5328&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::user.auth.xboxlive.com::MBI_SSL&display=touch&response_type=token&locale=en"
# Do not change this
cService = webdriver.ChromeService(executable_path=driver_path)
# Modify chrome options if you want. Experimental options i added was for testing and i left it like that.
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--lang=en')
options.add_argument("--disable-blink-features=AutomationControlled") 
options.add_argument('--log-level=1') # More suppressing shi that hoping it will work
options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"]) # Disabled logging cuz stupid
options.add_experimental_option("useAutomationExtension", False) 

# Put your XAG api token here
XAGtoken = ""

print(Fore.RED + r"""
 ____  __   __ _   _   ____ __        __   _     ____   _____ 
/ ___| \ \ / /| \ | | / ___|\ \      / /  / \   |  _ \ | ____|
\___ \  \ V / |  \| || |     \ \ /\ / /  / _ \  | |_) ||  _|  
 ___) |  | |  | |\  || |___   \ V  V /  / ___ \ |  _ < | |___ 
|____/   |_|  |_| \_| \____|   \_/\_/  /_/   \_\|_| \_\|_____|
                                                               
    """)
print(Style.RESET_ALL)
print(Fore.GREEN + "İnce bi' yağmur, caddem anlık")
print(Fore.GREEN + " ")
print(Fore.LIGHTCYAN_EX + "[XGPC Redeemer]")
print(Fore.GREEN + " ")
print(Fore.LIGHTCYAN_EX + "[1] Pre-check your codes")
print(Fore.LIGHTCYAN_EX + "[2] Run redeemer")
print(Fore.LIGHTRED_EX + "Changelog: rewrite strings")
print(Style.RESET_ALL) 

driver = webdriver.Chrome(service=cService, options=options)
def get_random_line(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        return random_line.strip()
    
def Type_Me(element: WebElement, text: str):
    for character in text:
        element.send_keys(character)
        sleep(uniform(.02, .06)) # If you want you can change .02 and .06 to lower/higher values to increase/decrease typing speed on Sign In page
wait = WebDriverWait(driver, 1000) # Default timeout.

def generateAccount():
    # These are disabled because i believe causes IP based ratelimits.
    # ===============================================================
    # ===============================================================

    #   Warning: THIS SHIT USES OLD API V1 I DIDNT UPDATE IT LOL
    #             | Check for stock  |
    #   url = "https://start-pasting.today/api/stock"
    #   response = requests.get(url)
    #   data = response.json()
   
    #   normal_accounts = data["normal_accounts"]
    #   print(str(normal_accounts) + " accounts in XAG")
   
    #            | Check for balance |
    #   url = "https://start-pasting.today/api/coins"
    #   response = requests.get(url, headers=headers)
    
    #   data = response.json()
   
    #   balance = data["coins"]
    #   print(str(balance) + " balance")
    # ===============================================================
    
    # Generate an account
    headers = {
    "Authorization": XAGtoken
    }
    while True:
        try:
            url = "https://start-pasting.today/v2/api/generate?type=xbox"
            response = requests.post(url, headers=headers)
            data = response.json()
            account = data["account"]["details"]
            global emailid
            global passwordid
            emailid = account["email"]
            passwordid = account["password"]
            username = account["username"]["is_set"]
            print(Fore.YELLOW+"[XAG] " + Fore.GREEN + emailid + ":" + passwordid)
            break
        except:
            print(Fore.RED + "Failed to generate account, more details: " + response.text)
            sleep(2)
            if "Account locked" in response.text:
                print(Fore.YELLOW+"[XAG] " +Fore.RED + "Account was locked, generating another one...")
                print(Style.RESET_ALL)
                
            if "Out of Stock" in response.text:
                print(Fore.YELLOW+"[XAG] " +Fore.RED + "No stock, please wait for restock.")
                print(Style.RESET_ALL)
                exit()
            if response.status_code == 429:
                print(Fore.YELLOW+"[XAG] " +Fore.RED + "Rate limited, exiting")
                exit()
    url = "https://xbox.com/en-US/auth/msa?action=logIn"
    driver.get(url)
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="loginfmt"]'))) 
    Type_Me(element, emailid)
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
    element.click()
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="passwd"]'))) 
    Type_Me(element, passwordid)
    sleep(1)
    try:
        element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
        
        element.click()
    except:
        pass
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="declineButton"]')))
    element.click()
    # Manual gamertag creation because api did not let me lmfao
    if username == False:    
        WebDriverWait(driver, 600000).until(EC.title_contains('Welcome to Xbox'))
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-1"]')))
        button.click()
        sleep(2)
        try:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
            button.click()
        except:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-2"]')))
            button.click()
            sleep(2)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
            button.click()
        
        #                               | Consent |                                 #
        wait.until(EC.title_contains('Consent'))
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
        button.click()
        wait.until(EC.title_contains('Xbox Official'))
    sleep(2)

def preCheckCodes(token):
    with open("codes.txt", "r") as file:
        codes = [line.strip() for line in file]
    valid_count = 0
    used_count = 0
    invalid_count = 0

    if len(codes) == 0:
        print(Fore.RED + "No codes found in codes.txt")
        input("Press Enter to exit...")
        print(Style.RESET_ALL)
        exit()
    print(Fore.LIGHTCYAN_EX + f"Loaded {len(codes)} codes")
    print(Fore.LIGHTCYAN_EX + " ")
    print(Style.RESET_ALL)
    input("Press Enter to start checking codes... | This will remove all invalid codes from your codes.txt!")    
    for code in codes:
        url = "https://emerald.xboxservices.com/xboxcomfd/buddypass/ValidateOfferRedeemer?market=US&offerId=" + code

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "authorization": token,
            "ms-cv": "Vm15+ysrWjVTvjwVU6gQBq.11",
            "x-ms-api-version": "1.0",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Priority": "u=4"
        }
 

        response = requests.get(url, headers=headers)
        if response.status_code == 401:
            print(Fore.RED + "[CHCK] Invalid token")
            input("Press Enter to exit...")
            print(Style.RESET_ALL)
            exit()
        if response.text == "\"ClaimedOffersMaxed\"":
            used_count += 1
            print(Fore.YELLOW + f"[-] {code} is used ({used_count})")
            with open("codes.txt", "r") as f:
                lines = f.readlines()
            with open("codes.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != code:
                        f.write(line)

        elif response.text == "\"OfferValid\"":
            valid_count += 1
            print(Fore.GREEN + f"[+] {code} is eligible ({valid_count})")
            
        elif response.text == "\"OfferNotFound\"":
            invalid_count += 1
            print(Fore.RED + f"[-] {code} is invalid ({invalid_count})") 
            with open("codes.txt", "r") as f:
                lines = f.readlines()
            with open("codes.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != code:
                        f.write(line)

        elif response.text == "\"OfferAlreadyClaimed\"":
            invalid_count += 1
            print(Fore.RED + f"[-] {code} is used ({used_count})")
            with open("codes.txt", "r") as f:
                lines = f.readlines()
            with open("codes.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != code:
                        f.write(line)

        else:
            print(Fore.RED + f"? {code} is {response.text}")   

    print(Fore.RED + f"- Invalid Codes: {invalid_count}")
    print(Fore.GREEN + f"+ Valid Codes: {valid_count}")
    print(Fore.YELLOW + f"- Used Codes: {used_count}")
    print(Style.RESET_ALL)
    input("Press Enter to exit...")
    print(Style.RESET_ALL)
    exit()

    
def get_urlPost_sFTTag(session):
    global retries
    while True: #will retry forever until it gets a working request/url.
        try:
            r = session.get(sFTTag_url, timeout=15)
            text = r.text
            match = re.match(r'.*value="(.+?)".*', text, re.S)
            if match is not None:
                sFTTag = match.group(1)
                match = re.match(r".*urlPost:'(.+?)'.*", text, re.S)
                if match is not None:
                    return match.group(1), sFTTag, session
        except: pass
        


def read_first_line(path):
    with open(path, "r") as file:
        return file.readline()


def delete_first_line(path):
    with open(path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.writelines(lines[1:])
        file.truncate()

def get_xbox_rps(session, email, password, urlPost, sFTTag):
            global bad, checked, cpm, twofa, retries, checked
            data = {'login': email, 'loginfmt': email, 'passwd': password, 'PPFT': sFTTag}
            login_request = session.post(urlPost, data=data, headers={'Content-Type': 'application/x-www-form-urlencoded'}, allow_redirects=True, timeout=15)
            if '#' in login_request.url and login_request.url != sFTTag_url:
                token = parse_qs(urlparse(login_request.url).fragment).get('access_token', ["None"])[0]
                
                if token != "None":
                    return token, session
            elif 'cancel?mkt=' in login_request.text:
                data = {
                    'ipt': re.search('(?<=\"ipt\" value=\").+?(?=\">)', login_request.text).group(),
                    'pprid': re.search('(?<=\"pprid\" value=\").+?(?=\">)', login_request.text).group(),
                    'uaid': re.search('(?<=\"uaid\" value=\").+?(?=\">)', login_request.text).group()
                }
                ret = session.post(re.search('(?<=id=\"fmHF\" action=\").+?(?=\" )', login_request.text).group(), data=data, allow_redirects=True)
                fin = session.get(re.search('(?<=\"recoveryCancel\":{\"returnUrl\":\").+?(?=\",)', ret.text).group(), allow_redirects=True)
                token = parse_qs(urlparse(fin.url).fragment).get('access_token', ["None"])[0]
                if token != "None":
                    return token, session
def mc_token(session, uhs, xsts_token):
    global retries
    while True:
        try:
            mc_login = session.post('https://api.minecraftservices.com/authentication/login_with_xbox', json={'identityToken': f"XBL3.0 x={uhs};{xsts_token}"}, headers={'Content-Type': 'application/json'}, timeout=15)
            if mc_login.status_code == 429:
                continue
            else:
                return mc_login.json().get('access_token')
        except:
           
            continue

def authenticate(email, password, tries = 0):
    global retries, bad, checked, cpm
    try:
        session = requests.Session()
        session.verify = True
        urlPost, sFTTag, session = get_urlPost_sFTTag(session)
        token, session = get_xbox_rps(session, email, password, urlPost, sFTTag)
        if token != "None":
            hit = False
            try:
                xbox_login = session.post('https://user.auth.xboxlive.com/user/authenticate', json={"Properties": {"AuthMethod": "RPS", "SiteName": "user.auth.xboxlive.com", "RpsTicket": token}, "RelyingParty": "http://auth.xboxlive.com", "TokenType": "JWT"}, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, timeout=15)
                js = xbox_login.json()
                xbox_token = js.get('Token')
                if xbox_token != None:
                    uhs = js['DisplayClaims']['xui'][0]['uhs']
                    xsts = session.post('https://xsts.auth.xboxlive.com/xsts/authorize', json={"Properties": {"SandboxId": "RETAIL", "UserTokens": [xbox_token]}, "RelyingParty": "rp://api.minecraftservices.com/", "TokenType": "JWT"}, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}, timeout=15)
                    js = xsts.json()
                    xsts_token = js.get('Token')
                    if xsts_token != None:
                        access_token = mc_token(session, uhs, xsts_token)
                        if access_token != None:
                            return access_token
            except: pass
            
    except:
       print(Fore.YELLOW+"[MCAUTH] " +Fore.RED+f"Failed to namechange: {email}:{password}")
    finally:
        session.close()
def fetchAccount():
    global emailid
    global passwordid
    try:
        combo = read_first_line("outlooks.txt")
        emailid = combo.split(":")[0]
        passwordid = combo.split(":")[1]
        delete_first_line("outlooks.txt")
        print(Fore.YELLOW+"[CHCK] " +"Fetched from outlooks.txt | "+ Fore.GREEN + emailid + ":" + passwordid)
    except:
        print("No more accounts in outlooks.txt, or you have a damaged file.")
        exit()
    url = "https://xbox.com/en-US/auth/msa?action=logIn"
    driver.get(url)
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="loginfmt"]'))) 
   
    Type_Me(element, emailid)
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
    element.click()
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@name="passwd"]'))) 
    
    Type_Me(element, passwordid)
    
    sleep(1)
    try:
        element = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="idSIButton9"]'))) 
        
        element.click()
    except:
        pass
    sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="declineButton"]')))
    element.click()
    sleep(2)
    try:
        WebDriverWait(driver, 15).until(EC.title_contains('Welcome to Xbox'))
        sleep(2)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-1"]')))
        button.click()
        sleep(2)
        try:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
            button.click()
        except:
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create-account-gamertag-suggestion-2"]')))
            button.click()
            sleep(2)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
            button.click()
        
        #                               | Consent |                                 #
        try:
            WebDriverWait(driver, 10).until(EC.title_contains('Consent'))
            sleep(2)
            button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inline-continue-control"]')))
            button.click()
        except:
            print(Fore.YELLOW+"[XBOX] " +"Skipping consent page (adjust).")
    except:
        print(Fore.YELLOW+"[XBOX] " +"Something went wrong while setting gamertag. Maybe it's already set? Skipping.")
        
    
    wait.until(EC.title_contains('Xbox Official'))
    sleep(2)
def redeemer():
    start = input(Fore.CYAN + "Type 'start' to begin. \n"+Fore.LIGHTCYAN_EX+ "Accepted flags are: \n \"--autoname\" (Sets profile automatically) \n \"--fromfile\" (Use outlooks.txt instead of XAG, must be no gamertag set) \n"+Fore.YELLOW+" Warning: FLAGS ARE IN DEVELOPMENT, YOU MAY ENCOUNTER BUGS. \n > ")
    if start.startswith('start'):
        if "--fromfile" in start:
            fetchAccount()
        else:
            generateAccount()
            
        codes = []
        with open('codes.txt', 'r') as file:
            for line in file:
                code = line.strip()
                codes.append(code)
        valid_count = 0
        for code in codes:
            
            url = f'https://www.xbox.com/en-US/xbox-game-pass/invite-your-friends/redeem?offerId={code}' 
           
            driver.get(url)
           
            sleep(4)
            page_source2 = re.sub(r'<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>', '', driver.page_source)
            

            if 'Redeem your 14-day trial, then install the Xbox app to start playing.' in str(page_source2):
                print(Fore.YELLOW + "[REDEEM] " + Fore.GREEN + f'Code {code} is eligible')
               
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
                wait.until(EC.presence_of_element_located((By.ID, "accountToken")))
                sleep(1)
                #                           ======================================                      #
                #       From this point, this beautiful and organized code with error handling is pasted from bubbb_  #
                driver.find_element(By.ID, "address_line1").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "address_line1").send_keys(Keys.DELETE)
                driver.find_element(By.ID, "city").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "city").send_keys(Keys.DELETE)
                driver.find_element(By.ID, "input_region").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "input_region").send_keys(Keys.DELETE)
                driver.find_element(By.ID, "postal_code").send_keys(Keys.CONTROL + "a")
                driver.find_element(By.ID, "postal_code").send_keys(Keys.DELETE)
                driver.find_element(By.ID, "address_line1").send_keys("9027 Fairground Circle")
                driver.find_element(By.ID, "city").send_keys("Oceanside")
                driver.find_element(By.ID, "input_region").send_keys("New York")
                driver.find_element(By.ID, "postal_code").send_keys("11572")

                sleep(1)

                need_profile_address = False
                while True:

                    line = read_first_line("ccs.txt")
                    cc_info = line.split("|")
                    cc = cc_info[0]
                    cc_date1 = cc_info[1]
                    cc_cvv = cc_info[3]
                    delete_first_line("ccs.txt")

                    driver.find_element(By.ID, "accountToken").click()
                    driver.find_element(By.ID, "accountToken").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "accountToken").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "accountHolderName").click()
                    driver.find_element(By.ID, "accountHolderName").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "accountHolderName").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "input_expiryMonth").click()
                    driver.find_element(By.ID, "cvvToken").click()
                    driver.find_element(By.ID, "cvvToken").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "cvvToken").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "accountToken").send_keys(cc)
                    driver.find_element(By.ID, "accountHolderName").send_keys("Alex")
                    driver.find_element(By.ID, "input_expiryMonth").send_keys(cc_date1)
                    driver.find_element(By.ID, "input_expiryYear").send_keys("27")
                    driver.find_element(By.ID, "cvvToken").send_keys(cc_cvv)

                    driver.find_element(By.ID, "pidlddc-button-saveButton").click()

                    sleep(2)
                    worked = False
                    while True:
                        went_next = True
                        try:
                            went_next = driver.find_element(
                                By.XPATH, "//*[contains(text(),'Add profile address')]"
                            ).is_displayed()
                        except:
                            went_next = False

                        if went_next:
                            
                            worked = True
                            need_profile_address = True
                            break

                        went_next = True
                        try:
                            went_next = driver.find_element(
                            By.XPATH, "//*[contains(text(),'CHANGE')]"
                            ).is_displayed()
                        except:
                            went_next = False

                        if went_next:
                            worked = True
                            break

                        went_next = True
                        try:
                            driver.find_element(
                            By.XPATH, "//*[contains(@class,'pidlddc-errorstroke')]"
                            )
                        except NoSuchElementException:
                            went_next = False

                        if went_next:
                            print(Fore.YELLOW+"[REDEEM] " + Fore.RED + "[CARD_DECLINED] "+ Fore.YELLOW+"("  + cc + ")")
                            went_next = False
                            worked = False
                            break

                        sleep(2)

                    if worked:
                        break

                if need_profile_address:
                    driver.find_element(
                    By.XPATH, "//*[contains(text(),'Add profile address')]"
                    ).click()
                    wait.until(EC.presence_of_element_located((By.ID, "address_line1")))
                    sleep(1)
                    driver.find_element(By.ID, "address_line1").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "address_line1").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "address_line1").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "city").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "city").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "input_region").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "input_region").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "postal_code").send_keys(Keys.CONTROL + "a")
                    driver.find_element(By.ID, "postal_code").send_keys(Keys.DELETE)
                    driver.find_element(By.ID, "address_line1").send_keys("9027 Fairground Circle")
                    driver.find_element(By.ID, "city").send_keys("Oceanside")
                    driver.find_element(By.ID, "input_region").send_keys("New York")
                    driver.find_element(By.ID, "postal_code").send_keys("11572")
                    driver.find_element(By.ID, "pidlddc-button-saveButton").click()
                    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'pidlddc-button-addressUseButton')))
                    sleep(1)
                    save2 = driver.find_element(By.ID,"pidlddc-button-addressUseButton")
                    save2.click()
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "primary--wA51gMLW.base--HZtGIsEc")))
                sleep(1)
                cbf = driver.find_element(By.CLASS_NAME, 'primary--wA51gMLW.base--HZtGIsEc')
                cbf.click()
                sleep(30)
                #                            End of pasted code from bubbb_                            #

                
                global current_day
                global current_month
                current_day = datetime.datetime.now().day
                current_month = datetime.datetime.now().strftime("%b")
                print(Fore.YELLOW + '[REDEEMED_XGP] ' + Fore.GREEN + emailid + ':' + passwordid + ' | ' + str(current_month) + ' ' + str(current_day))
                print(Style.RESET_ALL)
                if "--autoname" in start:
                    name = "FurinaXGP_" + ''.join(random.choices(string.ascii_letters + string.digits, k=5))
                    print(Fore.YELLOW + '[MCAUTH] ' + Fore.LIGHTCYAN_EX +'Attempting to set profile: ' + emailid + ':' + passwordid + " | " + name)
                    
                    token = authenticate(emailid, passwordid)
                    
                    urlget = f"https://api.minecraftservices.com/entitlements/mcstore"

                    headersget = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'Content-Type': 'application/json'}
                    requests.get(urlget,headers=headersget)
                    
                    sleep(2)
                    url = f"https://api.minecraftservices.com/minecraft/profile"
                    body = {
                        "profileName": name
                    }
                    headers = {'Authorization': f'Bearer {token}', 'Accept': 'application/json', 'Content-Type': 'application/json'}
                    response = requests.post(url,headers=headers, json=body)
                    response_json = response.json()
                    if "ACTIVE" in str(response_json):
                        print(Fore.GREEN + "[MCAUTH] " + emailid + ' + Name changed to ' + name)
                        print(Style.RESET_ALL)
                    else:
                        print(Fore.RED + "[MCAUTH] " + emailid + ' - Name change failed:')
                        print(response_json)
                        print(Style.RESET_ALL)
                
                with open('unbans.txt', 'a') as file:
                    file.write(emailid + ':' + passwordid + '\n')
                
                sleep(2)
                driver.get('https://www.xbox.com/en-US/auth/msa?action=logOut')
                sleep(3)
                driver.delete_all_cookies()
                sleep(1)
              
                if "--fromfile" in start:
                    fetchAccount()
                else:
                    generateAccount()
    # Please dont test me >_<
Input = input(">")
if Input == "1":
    xbltoken = input(Fore.BLUE + "Enter your XBL token:")
    preCheckCodes(xbltoken)
if Input == "2":
    redeemer()
    driver.quit()
    print(Fore.YELLOW + 'End of codes!')
    print(Style.RESET_ALL)

