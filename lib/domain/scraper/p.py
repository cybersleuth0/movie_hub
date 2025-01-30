import os
import time
import pyfiglet
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import ssl
import json

try:
    ssl._create_default_https_context = ssl._create_unverified_context
except AttributeError:
    pass

os.system("cls")
banner = pyfiglet.figlet_format("HDHub4U Scraper")
print(banner)

try:
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    action = ActionChains(driver)

    url = "https://hdhub4u.how/vikings-valhalla-season-3-hindi-webrip-all-episodes/"
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    driver.execute_script("scrollBy(0, 650)")
    time.sleep(2)

    result = {}
    try:
        movie_poster = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/p[2]/img"))).get_attribute("src")
        result["movie_Poster"] = movie_poster
    except Exception as e:
        print("Error extracting movie poster:", e)

    try:
        movie_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/h2")))
        result["movie_Name"] = movie_name_element.text
    except Exception as e:
        print("Error extracting movie name:", e)

    try:
        desc_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]")))
        desc_text = desc_element.text.replace("\n", " ").strip()
        result["movie_desc"] = desc_text
    except Exception as e:
        print("Error extracting movie description:", e)

    try:
        screenshots_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/h3")))
        screenshot_links = [img.get_attribute("src") for img in screenshots_element.find_elements(By.TAG_NAME, "img")]
        result["movie_screenshot_links"] = screenshot_links
    except Exception as e:
        print("Error extracting screenshots:", e)

    try:
        download_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section/div/section/main/div[3]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]//a")))
        download_links = [{"text": el.text, "url": el.get_attribute("href")} for el in download_elements]
        result["movie_download_links"] = download_links
    except Exception as e:
        print("Error extracting download links:", e)

    print(json.dumps(result, indent=2))

finally:
    driver.quit()
