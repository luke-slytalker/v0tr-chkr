import requests
from bs4 import BeautifulSoup
import time

##############
# USE:  python3 main.py > output_file.txt
# 
# I'll make it more user-friendly this weekend
# but for now, we can start sraping and building databases.
# URL format:  /voters/<state>/search+filter/<page>
#               /voters/mi/before+1930/2


url = "https://voterrecords.com/voters/mi/before+1930/"     # base search URL
headers = {'User-Agent': 'Mozilla/5.0'}                     # headers so it doesn't think we're scraping

pages = 26375       # how many pages there are according to the website.
x = 1

while x < pages:
    page_to_scrape = url + str(x)
    response = requests.get(page_to_scrape, headers=headers)    # create the http request & store the data in "response"
    soup = BeautifulSoup(response.text, "html.parser")       # initialize a BS object that's intending to parse HTML
    table = soup.find('table')
    rows = ""
    for tr in table.find_all('tr', itemtype="http://schema.org/Person"):  # iterate thru all the TR tags
        the_name = tr.span.span.a.span.text
        print("-----------------")
        print(the_name)
        for tds in tr.find_all('td', class_='hidden-xs'):
            if len(tds.text) > 33:  # filter out tags with no text
                data = tds.text.strip()  # strip out any extra RETURNS
                print(data)

    x += 1
    time.sleep(.17)
