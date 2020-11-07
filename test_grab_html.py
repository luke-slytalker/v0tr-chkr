import requests
from bs4 import BeautifulSoup
import time

url = "https://voterrecords.com/voters/mi/before+1930/"     # base search URL
headers = {'User-Agent': 'Mozilla/5.0'}                     # headers so it doesn't think we're scraping

pages = 1166962
x = 1

while x < pages:
    page_to_scrape = url + str(x)
    response = requests.get(page_to_scrape, headers=headers)    # create the http request & store the data in "response"
    soup = BeautifulSoup(response.content, "html.parser")       # initialize a BS object that's intending to parse HTML
    table = soup.find('table')
    #for tr in table.find_all('tr'):  # iterate thru all the TR tags
    #    spans = tr.find_all('span')
    #    #spans = tr.find_all('span', itemprop="name")
    #    for s in spans:
    #        print(s)

    f = open("MI_born_b4_1930.txt", "a")
    f.write(str(table))
    f.close()
    time.sleep(.17)

    x += 1

