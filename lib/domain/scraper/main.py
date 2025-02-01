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
    "https://hdhub4u.how/the-curse-of-la-llorona-2019-bluray-hindi-org-5-1-english-1080p-720p-480p-dual-audio-x264-esubs-full-movie/",
"https://hdhub4u.how/the-nun-2018-org-hindi-dual-audio-720p-bluray-1-2gb/",
"https://hdhub4u.how/annabelle-comes-home-2019-org-hindi-dual-audio-720p-bluray-850-mb/",
"https://hdhub4u.how/annabelle-creation-2017-hindi-dual-audio-720p-bluray-950mb/",
"https://hdhub4u.how/annabelle-2014-bluray-hindi-english-full-movie/",
"https://hdhub4u.how/the-conjuring-3-2021-hindi-org-bluray-full-movie/",
"https://hdhub4u.how/the-conjuring-2-2016-bluray-hindi-english-full-movie/",
"https://hdhub4u.how/the-conjuring-2013-bluray-hindi-english-full-movie/",
"https://hdhub4u.how/alive-2020-webrip-full-movie/",
"https://hdhub4u.how/hellboy-2019-bluray-hindi-english/",
"https://hdhub4u.how/grafted-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/azrael-2024-hindi-bluray-full-movie/",
"https://hdhub4u.how/nosferatu-2024-webrip-english-full-movie/",
"https://hdhub4u.how/the-silence-of-the-lambs-1991-bluray-hindi/",
"https://hdhub4u.how/hellboy-the-crooked-man-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/the-witch-revenge-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/apartment-7a-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/bloody-axe-wound-2024-webrip-english-full-movie/",
"https://hdhub4u.how/dominion-prequel-to-the-exorcist-2005-bluray-hindi-english-full-movie/",
"https://hdhub4u.how/truth-or-dare-2018-hindi-bluray/",
"https://hdhub4u.how/nishabdham-2020-uncut-hindi-webrip-full-movie/",
"https://hdhub4u.how/gogol-a-terrible-vengeance-2018-hindi-bluray-full-movie/",
"https://hdhub4u.how/gogol-viy-2018-hindi-bluray-full-movie/",
"https://hdhub4u.how/bhool-bhulaiyaa-3-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/spiders-2023-webrip-hindi-french-movie/",
"https://hdhub4u.how/the-crow-2024-hindi-bluray-full-movie/",
"https://hdhub4u.how/cuttputlli-2022-webrip-hindi-full-movie/",
"https://hdhub4u.how/dancing-village-the-curse-begins-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/the-exorcism-of-emily-rose-2005-unrated-hindi-bluray-full-movie/",
"https://hdhub4u.how/dont-turn-out-the-lights-2023-hindi-webrip-full-movie/",
"https://hdhub4u.how/never-let-go-2024-hindi-bluray-full-movie/",
"https://hdhub4u.how/sting-2024-hindi-bluray-full-movie/",
"https://hdhub4u.how/kalinga-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/bagman-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/mononoke-the-movie-the-phantom-in-the-rain-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/from-season-3-hindi-webrip-all-episodes/",
"https://hdhub4u.how/smile-2-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/alien-romulus-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/operation-blood-hunt-2024-hindi-webrip-full-movie/",
"https://hdhub4u.how/smile-2022-bluray-hindi-org-5-1-english-1080p-720p-480p-dual-audio-x264-full-movie/",
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
            desc_text = desc_element.text.strip()
            result["movie_desc"] = desc_text
        except Exception as e:
            print("Error extracting movie description:", e)

        # Extract movie screenshots
        try:
            screenshots_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section/div/section/main/h3"))
            )
            screenshot_links = [
                img.get_attribute("src") for img in screenshots_element.find_elements(By.TAG_NAME, "img")
            ]
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
                {el.text.strip():el.get_attribute("href")}
                for el in download_elements if el.get_attribute("href")
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
