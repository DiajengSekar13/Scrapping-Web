from bs4 import BeautifulSoup
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Query to obtain links
query = "Joko Widodo"

# links = [] # initiate empty list to capture final result
# specify number of pages on google search, each page contains 10 #links
n_pages = 2

for page in range (1, n_pages):
    url = "http://www.google.com/search?q=" + query + "&start=" + str((page - 1)*10)
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # soup = BeautifulSoup(r.text, 'html.parser')

    search = soup.find_all('div', class_="yuRUbf")
    for h in search:
        # links.append(h.a.get('href'))
        # print(h.a.text)
        print(h.a.get('href'))