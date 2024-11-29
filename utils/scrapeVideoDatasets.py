import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

with open('../datasets/wordList.txt', 'r') as file:
    words = [line.strip() for line in file]
    print(words)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://pmpk.kemdikbud.go.id/sibi/pencarian')

def scrape_videos_for_word(word):
    search_box = driver.find_element(By.NAME, 'key')
    search_box.clear()
    search_box.send_keys(word)
    search_box.send_keys(Keys.RETURN)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    video_links = []

    video_links.append(soup.select_one('source').get('src'))

    return video_links

for word in words:
    url = scrape_videos_for_word(word)
    r = requests.get(url[0], stream = True)
    with open(f'../datasets/videos/{word}.webm', 'wb') as file:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                file.write(chunk)
    print(f"Downloaded video for {word}")
    driver.back()

driver.quit()