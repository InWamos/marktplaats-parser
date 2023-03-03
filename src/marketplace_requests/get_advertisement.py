import logging
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from src.data_handlers.json_data_handler import update_json_file
from src.classes.last_car_ad import LastCarAdvertisement
  
logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

def send_requests() -> list[LastCarAdvertisement]:

    items_list = []
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("./driver/chromedriver", options=options)

    try:
        driver.get("https://www.marktplaats.nl/l/auto-s/#constructionYearFrom:2006|PriceCentsFrom:100000|PriceCentsTo:1000000|sortBy:SORT_INDEX|sortOrder:DECREASING")
        time.sleep(2)

        consent_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[1]")
        consent_button.click()
        time.sleep(2)

        gallery_div = driver.find_element(By.CSS_SELECTOR, "ul.hz-Listings:nth-child(3)")
        gallery_items = gallery_div.find_elements(By.TAG_NAME, "li")

        for i, k in enumerate(gallery_items):
            try:
                link_to_add = k.find_element(By.TAG_NAME, "a")
                item_name = driver.find_element(By.CSS_SELECTOR, f'li.hz-Listing:nth-child({i + 1}) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1)').text
            
                item_link = link_to_add.get_attribute('href')
                
                print(f"{i}: {item_name}: {item_link}")
            except:
                print(i)
                pass
            

    finally:
        driver.quit()