# aozora_scrapper_service.py

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class AozoraScapper():
    story_limit = 10

    baseurl = 'https://www.aozora.gr.jp/'

    def get_link(self):
        driver = webdriver.Firefox()

        driver.get(self.baseurl)
        link = driver.find_element(By.XPATH, "//td[@class='summary']/a").get_attribute("href")
        driver.get(link)
        sleep(2)
        links = driver.find_elements(By.XPATH, "//ol/li/a")

        hits = 0
        download_links = []

        for link in links:
            if hits == 5: 
                break

            href = link.get_attribute('href')
            sleep(2)

            # Move one page forward
            driver.get(href)
            sleep(2)

            try:
                next_link = driver.find_element(By.XPATH, "//ol/li/a").get_attribute("href")

                # Move another page forward
                driver.get(next_link)
                sleep(2)

                # Use WebDriverWait to wait for the download table to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, 
                            "//table[@class='download']//a[contains(@href, '.html')]"))
                )
                # Attempt to find the download link
                download = driver.find_element(By.XPATH, 
                                "//table[@class='download']//a[contains(@href, '.html')]").get_attribute('href')
                print(download)
                download_links.append(download)
                hits += 1

            except (NoSuchElementException, TimeoutException):
                print("Download link not found or timed out on this page. Moving on to the next one.")

            # Go back two pages
            driver.back()
            driver.back()
            sleep(5)
        
        return download_links


if __name__ == "__main__":
    AS = AozoraScapper()
    download = AS.get_link()
