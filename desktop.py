import urllib.request as urllib3
from bs4 import BeautifulSoup
import json

aqi_page = 'https://cfpub.epa.gov/airnow/state/CA/index.cfm'
page = urllib3.urlopen(aqi_page)
soup = BeautifulSoup(page, "html5lib")

cities = []
city_box = soup.findAll('a', attrs={'class': 'NtnlSummaryCity'})
for city in city_box:
	cities.append(city.string)

aqis = []
aqi_box = soup.findAll('td', attrs={'style': 'text-align:center'})
for aqi in aqi_box:
	aqis.append(aqi.string)

dictionary = dict(zip(cities, aqis))

output_json = json.dumps(
	dictionary, sort_keys=True, indent=4, separators=(',', ': '))

print(output_json)
""" print(dictionary) """
""" with open('output.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(dictionary) """

