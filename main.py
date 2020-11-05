import requests
from bs4 import BeautifulSoup

url = "https://voterrecords.com/voters/mi/before+1930/"     # search URL
headers = {'User-Agent': 'Mozilla/5.0'}                     # headers so it doesn't think we're scraping
response = requests.get(url, headers=headers)           # create the http request & store the data in "response"
soup = BeautifulSoup(response.content, "html.parser")   # initialize a BS object that's intending to parse HTML

# format is:  /voters/<state>/<search+term>/<page number>
# /voters/mi/before+1930/6  == page 6 of the search results for MI voters born before 1930


# grabbing the number of pages was insanely more difficult than it should have been
# BS4 wouldn't find the #pageBar ID for the DIV, so I had to get creative...
x = list()
for label in soup.find_all('label'):
    x.append(label.text)

num_of_pages = x[4][10:]
pages = num_of_pages.replace(',', '')

# we need to look for the first table in the HTML--it's where the voter info is inserted from their DB
table = soup.find('table')

for tr in table.find_all('tr'):     # iterate thru all the TR tags
    tds = tr.find_all('td')
    print(tds)

