from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_data(base_url, category, location, additionalFilters):
    url = "/".join([base_url, category, location]) + "/" + "&".join(additionalFilters)
    
    browser_driver = Service('/usr/lib/chromium-browser/chromedriver')
    browser = webdriver.Chrome(service=browser_driver)
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    
    listings = soup.find_all("div", {"data-cy":"l-card"})
    items = []
    for listing in listings:
        item = {}
        item['listing_title'] = listing.find("h6").string
        item['listing_price'] = listing.find("p", {"data-testid":"ad-price"}).text.strip()
        item_location_and_date = listing.find("p", {"data-testid":"location-date"}).text.strip()
        item['location'] = item_location_and_date.split("-", 1)[0]
        item['date'] = item_location_and_date.split("-", 1)[-1]
        item['link'] = listing.find("a", href=True)['href']
        items.append(item)
    browser.close()
    return items
    
