import logging
import time
import asyncio

from selenium import webdriver
from selenium.webdriver.common.by import By
from src.data_handlers.json_data_handler import update_json_file
from src.classes.car_ad import CarAdvertisement
  
logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

def get_links() -> list[str]:
    """Parses .txt with links   

    Returns:
        list: list of parsed links from txt
    """

    with open('links.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()
    
    return links

def get_advertisements_from_page(
        link_to_page: str) -> list[CarAdvertisement]:

    items_list = []
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome("./driver/chromedriver", options=options)

    try:
        driver.get(link_to_page)
        time.sleep(2)

        consent_button = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/button[1]")
        consent_button.click()
        time.sleep(2)

        gallery_div = driver.find_element(By.CSS_SELECTOR, "ul.hz-Listings:nth-child(3)")
        gallery_items = gallery_div.find_elements(By.TAG_NAME, "li")

        for i, k in enumerate(gallery_items):
            try:
                item_anchor = k.find_element(By.TAG_NAME, "a")
                item_name = driver.find_element(By.CSS_SELECTOR, f'li.hz-Listing:nth-child({i + 1}) > a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > h3:nth-child(1)').text
                item_link = item_anchor.get_attribute('href')

                items_list.append(CarAdvertisement(
                    link_to_page=link_to_page,
                    link_to_item=item_link,
                    name=item_name
                ))
                print(f"{i}: {item_name}")
            except:
                continue
        

    finally:

        driver.quit()
        return items_list
    
async def get_advertisements_from_page_loop(send_update: object) -> None:
    """Function to put inside the loop in main.py

    Args:
        send_update (object): Bot's method send_message_on_update()
    """
    while True:
        try:
            links = get_links()
            await asyncio.sleep(10)

            for i in links:
                try:
                    items_list = get_advertisements_from_page(i)
                    
                    if items_list:
                        
                        await update_json_file(
                            last_offers=items_list,
                            send_update=send_update
                        )

                except:
                    logging.exception(
                        msg="Non-critical error in get_advertisement.py in get_advertisements_from_page_loop",
                        exc_info=True
                        )
        finally:
            await asyncio.sleep(50)         