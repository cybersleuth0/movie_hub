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

# Clear console and display banner
os.system("cls")
banner = pyfiglet.figlet_format("HDHub4U Scraper")
print(banner)

# List to store all results
all_results = []

# List of URLs to scrape
urls = [
    "https://hdhub4u.how/den-of-thieves-2-pantera-2025-english-webrip-full-movie/",
    "https://hdhub4u.how/flight-risk-2025-hdts-english-full-movie/",
    "https://hdhub4u.how/fateh-2025-hindi-webrip-full-movie/",
    "https://hdhub4u.how/cid-season-2-hindi-webrip-all-episodes/",
    "https://hdhub4u.how/eagle-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/law-abiding-citizen-2009-bluray-hindi-english/",
    "https://hdhub4u.how/sky-force-2025-hindi-pre-hd-full-movie/",
    "https://hdhub4u.how/twilight-of-the-warriors-walled-in-2024-bluray-hindi-chinese-full-movie/",
    "https://hdhub4u.how/game-changer-2025-hindi-webrip-full-movie/",
    "https://hdhub4u.how/bhaje-vaayu-vegam-2024-uncut-hindi-webrip-full-movie/",
    "https://hdhub4u.how/the-sand-castle-2025-webrip-english-full-movie/",
    "https://hdhub4u.how/hisaab-barabar-2025-hindi-webrip-full-movie/",
    "https://hdhub4u.how/the-night-agent-season-2-hindi-webrip-all-episodes/",
    "https://hdhub4u.how/grafted-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/azrael-2024-hindi-bluray-full-movie/",
    "https://hdhub4u.how/the-bourne-ultimatum-2007-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/the-bourne-supremacy-2004-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/the-bourne-legacy-2012-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/the-bourne-identity-2002-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/pottel-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/the-killers-game-2024-hindi-bluray-full-movie/",
    "https://hdhub4u.how/garudan-2023-uncut-hindi-webrip-full-movie/",
    "https://hdhub4u.how/table-no-21-2013-hindi-movie-720p-dvdrip-950mb/",
    "https://hdhub4u.how/jason-bourne-2016-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/night-hunter-2018-hindi-bluray-full-movie/",
    "https://hdhub4u.how/pushpa-2-reloaded-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/the-silence-of-the-lambs-1991-bluray-hindi/",
    "https://hdhub4u.how/paatal-lok-season-2-hindi-webrip-all-episodes/",
    "https://hdhub4u.how/money-monster-2016-hindi-bluray-full-movie/",
    "https://hdhub4u.how/alarum-2025-webrip-english-full-movie/",
    "https://hdhub4u.how/rifle-club-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/pani-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/apartment-7a-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/dominion-prequel-to-the-exorcist-2005-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/the-calendar-killer-2025-webrip-hindi-english-full-movie/",
    "https://hdhub4u.how/kraven-the-hunter-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/khuda-haafiz-2020-webrip-hindi-full-movie/",
    "https://hdhub4u.how/truth-or-dare-2018-hindi-bluray/",
    "https://hdhub4u.how/sorgavaasal-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/shadow-land-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/nishabdham-2020-uncut-hindi-webrip-full-movie/",
    "https://hdhub4u.how/sookshmadarshini-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/97-minutes-2023-bluray-hindi-english-full-movie/",
    "https://hdhub4u.how/the-sabarmati-report-2024-proper-web-dl-hindi-dd5-1-4k-1080p-720p-480p-x264-hevc-full-movie/",
    "https://hdhub4u.how/ad-vitam-2025-webrip-hindi-english-full-movie/",
    "https://hdhub4u.how/ui-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/ugramm-2014-uncut-hindi-dual-audio-720p-hdrip-1gb/",
    "https://hdhub4u.how/american-primeval-season-1-hindi-webrip-all-episodes/",
    "https://hdhub4u.how/dashmi-2024-hindi-webrip-full-movie/",
    "https://hdhub4u.how/fake-profile-season-2-hindi-webrip-all-episodes/",
    "https://hdhub4u.how/dark-season-3-webrip-dual-audio/",
    "https://hdhub4u.how/dark-season-2/",
    "https://hdhub4u.how/dark-season-1/",
    "https://hdhub4u.how/gogol-a-terrible-vengeance-2018-hindi-bluray-full-movie/",
    "https://hdhub4u.how/the-man-on-the-road-2022-hindi-bluray-full-movie/",
    "https://hdhub4u.how/rangasthalam-2018-hindi-hq-dubbed-webrip-full-movie/"
]


# Initialize WebDriver
try:
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    action = ActionChains(driver)

    for url in urls:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        # Scroll to load content
        driver.execute_script("scrollBy(0, 650)")
        time.sleep(2)

        # Dictionary to store the scraped data for each movie
        result = {}

        # Extract movie poster
        try:
            movie_poster = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/p[2]/img"))
            ).get_attribute("src")
            result["movie_Poster"] = movie_poster
        except Exception as e:
            print("Error extracting movie poster:", e)

        # Extract movie name
        try:
            movie_name_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/h2"))
            )
            result["movie_Name"] = movie_name_element.text.strip()
        except Exception as e:
            print("Error extracting movie name:", e)

        # Extract movie description
        try:
            desc_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div[2]"))
            )
            desc_text = desc_element.text.replace("\n", " ").strip()
            result["movie_desc"] = desc_text
        except Exception as e:
            print("Error extracting movie description:", e)

        # Extract movie screenshots
        try:
            screenshots_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/h3")))
            screenshot_links = [img.get_attribute("src") for img in screenshots_element.find_elements(By.TAG_NAME, "img")]
            result["movie_screenshot_links"] = screenshot_links
        except Exception as e:
            print("Error extracting screenshots:", e)

        # Scroll to the download links section
        driver.execute_script("scrollBy(0, 2500)")

        # Extract movie download links
        try:
            download_elements = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "/html/body/section/div/section/main/div[3]//a")
                )
            )
            download_links = [
                {"text": el.text.strip(), "url": el.get_attribute("href")}
                for el in download_elements
                if el.get_attribute("href")
            ]
            result["movie_download_links"] = download_links
        except Exception as e:
            print("Error extracting download links:", e)

        # Append the result to the list
        all_results.append(result)
        print(json.dumps(result, indent=2))

finally:
    # Quit the driver
    driver.quit()

# Save all results to a JSON file
output_file = "results.json"
with open(output_file, "w") as f:
    json.dump(all_results, f, indent=2)

print(f"Results saved to {output_file}")
