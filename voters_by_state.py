############################
# scrape the voter info from voterrecords.com
# format of output looks like:
# -----------------
# First M Last
# Residential Address:
# Wasilla Ak 99654
# Mailing Address:
# Wasilla Ak 99654-1816
# Party Affiliation: Alaskan Independence Party
# -----------------
#  USAGE:   python3 voters_by_state.py state_abbrev > output.txt
#  EXAMPLE: python3 voters_by_state.py nv > nv_voters.txt

import requests
from bs4 import BeautifulSoup
import time
import sys

states = list()     # create a list and add all the (supported) states to it
states.append("ak")
states.append("ar")
states.append("co")
states.append("ct")
states.append("de")
states.append("dc")
states.append("fl")
states.append("la")
states.append("mi")
states.append("nc")
states.append("nv")
states.append("oh")
states.append("ok")
states.append("ri")
states.append("ut")
states.append("wa")

try:
    the_state = sys.argv[1]
except IndexError:
    print("Please Choose a State")
    st_string = ""
    for x in states:
        st_string += x + "  "
    print(st_string)
    quit()

for s in states:
    if s == the_state.lower():
        st = s

url = "https://voterrecords.com/voters/" + st + "/"  # base search URL
headers = {'User-Agent': 'Mozilla/5.0'}         # headers so it doesn't think we're scraping
response = requests.get(url, headers=headers)   # create the http request & store the data in "response"
soup = BeautifulSoup(response.text, "html.parser")   # initialize a BS object that's intending to parse HTML

testing = soup.find('div', id="PageBar")
num_of_pages = testing.label.text[10:]
pages = num_of_pages.replace(',', '')
#print(pages)
print("------- There are [ " + str(pages) + " ] pages of records -------")
x = 1

while x < int(pages):
    page_to_scrape = url + str(x)
    response = requests.get(page_to_scrape, headers=headers)    # create the http request & store the data in "response"
    soup = BeautifulSoup(response.text, "html.parser")       # initialize a BS object that's intending to parse HTML
    table = soup.find('table')
    rows = ""

    for tr in table.find_all('tr', itemtype="http://schema.org/Person"):    # iterate thru all the TR tags
        try:
            the_name = tr.span.span.a.span.text
            print("-----------------")
            print(the_name)
            for tds in tr.find_all('td', class_='hidden-xs'):
                if len(tds.text) > 33:          # filter out tags with no text
                    data = tds.text.strip()     # strip out any extra RETURNS
                    print(data)
        except TypeError:
            pass
    x += 1
    time.sleep(.17)
