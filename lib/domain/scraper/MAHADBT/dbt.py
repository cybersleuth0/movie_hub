import threading
import selenium
import time
import os
import random
import pyfiglet
import pyautogui
import openpyxl
from openpyxl import Workbook, load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from clicker import allok_clicker, decr_clicker, backclick, pursuing

os.system("cls")
driver_service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)
banner = pyfiglet.figlet_format("MAHADBT")
os.system("cls")
action = ActionChains(driver)
# ##################### LOGIN ############################
driver.get("https://hdhub4u.how/vikings-valhalla-season-3-hindi-webrip-all-episodes/")
driver.execute_script('scrollBy(0,650)')
time.sleep(2)
# username = input("Enter Username: ")
# passwd = input("Enter Password: ")
# driver.find_element(By.ID, "username").send_keys(username)
# driver.find_element(By.ID, "Userpassword").send_keys(passwd)
# captha = input("ENTER CAPTHA: ")
# captha.upper()
# driver.find_element(By.NAME, "CaptchaInputText").send_keys(captha)
# driver.execute_script('scrollBy(0,120)')
# time.sleep(0.5)
# driver.find_element(By.ID, "btnLogin").click()
# driver.execute_script('scrollBy(0,620)')
# time.sleep(1)
# url = driver.current_url
# if url == "https://dbtworkflow.mahaonline.gov.in/Home/HomePage":
#     print("Log in succesfull")
# elif url == "https://dbtworkflow.mahaonline.gov.in/":
#     driver.find_element(By.ID, "username").send_keys(username)
#     driver.find_element(By.ID, "Userpassword").send_keys(passwd)
#     captha = input("ENTER CAPTHA: ")
#     captha.upper()
#     driver.find_element(By.NAME, "CaptchaInputText").send_keys(captha)
#     driver.execute_script('scrollBy(0,120)')
#     time.sleep(0.5)
#     driver.find_element(By.ID, "btnLogin").click()
# ################################## Scrutiny ###########################
# driver.maximize_window()
# driver.get(
#     "https://dbtworkflow.mahaonline.gov.in/CollegeScrutinyDashBoard/Collegehomepage")
# time.sleep(5)
# os.system("cls")
# ans = input("Have you Enter all details Y or N:  ")
# if ans == 'y' or 'Y':
#     num = input("Enter loop num: ")
#     ############################ loop ###############################
#     for i in range(int(num)):
#         time.sleep(2)
#         driver.find_element(
#             By.CLASS_NAME, "dxeHyperlink").click()
#         time.sleep(1)
#         attendance_int = random.randrange(78, 85)
#         print(attendance_int)
#         driver.find_element(By.ID, "Attendance").send_keys(
#             Keys.CONTROL + 'a', Keys.BACKSPACE)
#         time.sleep(1)
#         driver.find_element(By.ID, "Attendance").send_keys(attendance_int)
#         time.sleep(0.2)
#         driver.execute_script('scrollBy(0,400)')
#         allok_clicker()
#         time.sleep(0.05)
#         decr_clicker()
#         time.sleep(0.05)
#         driver.execute_script('scrollBy(0,15)')
#         time.sleep(0.05)
#         driver.find_element(By.ID, "btn0").click()
#         time.sleep(2)
#         driver.find_element(By.CLASS_NAME, "confirm").click()
#         time.sleep(5)
# else:
#     print("Bye Bye")
#     exit()
