#aozora_scrapper_service.py

from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AozoraScapper():
    options = webdriver.FirefoxOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    story_limit = 10

    driver = webdriver.Firefox()

    baseurl = 'https://www.aozora.gr.jp/'

    def get_link(self):
        driver = self.driver
        driver.get(self.baseurl)
        link = driver.find_element(By.XPATH, "//td[@class='summary']/a").get_attribute("href")
        driver.get(link)
        sleep(2)
        links = driver.find_elements(By.XPATH, "//ol/li/a")

        hits = 0


        for link in links:
                href = link.get_attribute('href')
                sleep(5)
                driver.get(href)
                sleep(5)
                next_link = driver.find_element(By.XPATH, "//ol/li/a").get_attribute("href")
                driver.get(next_link)
                sleep(5)

                # Use WebDriverWait to wait for the download table to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, 
                            "//table[@class='download']//a[contains(@href, '.html')]"))
                )
                download = driver.find_element(By.XPATH, 
                            "//table[@class='download']//a[contains(@href, '.html')]").get_attribute('href')
                return download #returns the download link

if __name__ == "__main__":
    AS = AozoraScapper()
    download = AS.get_link()
    AS.driver.get(download)