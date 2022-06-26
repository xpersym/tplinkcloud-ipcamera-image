import time
import ftplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import os
from dotenv import load_dotenv
import warnings
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
warnings.filterwarnings("ignore", category=DeprecationWarning)


load_dotenv()

def kamera1():
    file_name='kamera1.png'
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(os.getenv('TPLINK_URL'));
    time.sleep(1)
    email = driver.find_element_by_id("Email")
    email.send_keys(os.getenv('TPLINK_USERNAME'))
    password = driver.find_element_by_id("Password")
    password.send_keys(os.getenv('TPLINK_PASSWORD'))
    time.sleep(1)
    l=driver.find_element_by_xpath('//*[@id="submit_btn"]')
    l.click();
    time.sleep(30)
    element = driver.find_element_by_xpath('//*[@id="JSVideo"]')
    element.screenshot(file_name)
    session = ftplib.FTP(os.getenv('FTP_HOST'),os.getenv('FTP_USER'),os.getenv('FTP_PASSWORD'))
    file = open(file_name,'rb')
    filename=f"{os.getenv('FTP_PATH')}{file_name}"
    path= f"STOR {os.getenv('FTP_PATH')}{file_name}"
    session.storbinary(path, file)
    session.sendcmd('SITE CHMOD 644 ' + filename)
    file.close()
    session.quit()
    driver.quit()
    print(f"[{current_time}] Kamera 1 Done")


def kamera2():
    file_name='kamera2.png'
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(os.getenv('TPLINK_URL'));
    time.sleep(1)
    email = driver.find_element_by_id("Email")
    email.send_keys(os.getenv('TPLINK_USERNAME'))
    password = driver.find_element_by_id("Password")
    password.send_keys(os.getenv('TPLINK_PASSWORD'))
    time.sleep(1)
    l=driver.find_element_by_xpath('//*[@id="submit_btn"]')
    l.click()
    time.sleep(30)
    kamera2id=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/ul/li[2]');
    kamera2id.click()
    time.sleep(15)
    element = driver.find_element_by_xpath('//*[@id="JSVideo"]')
    element.screenshot(file_name)
    session = ftplib.FTP(os.getenv('FTP_HOST'),os.getenv('FTP_USER'),os.getenv('FTP_PASSWORD'))
    file = open(file_name,'rb')
    filename=f"{os.getenv('FTP_PATH')}{file_name}"
    path= f"STOR {os.getenv('FTP_PATH')}{file_name}"
    session.storbinary(path, file)
    session.sendcmd('SITE CHMOD 644 ' + filename)
    file.close()
    session.quit()
    driver.quit()
    print(f"[{current_time}] Kamera 2 Done")


while 1:
    kamera1()
    kamera2()
    time.sleep(900)
