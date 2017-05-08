#!/usr/bin/env python
__author__ = "Kevin Orr"

# suck in the 'requests' module for doing http stuff - like pulling down the html
import requests
# for parsing the html we'll use BeautifulSoup
from bs4 import BeautifulSoup

def get_country_codes():
    map = dict()
    r = requests.get('https://countrycode.org/')
    soup = BeautifulSoup(r.text, 'html.parser')

    #  now lets pull out the table rows...
    rows = soup.table.tbody.find_all('tr')
    # and run over the collection of rows to get the country name and it's associated ISO code
    for row in rows:
        [name, code, iso, population, areaKm, gdp] = row.find_all('td')
        map[name.text.lower().strip()] = (name.text, code.text, iso.text, population.text, areaKm.text, gdp.text)

    return map


if __name__ == '__main__':
    map = get_country_codes()
    country = str(raw_input("Give me a bleeding country name will ye...>> "))
    while country != "fuck off":
        if country in map.keys():
            (name, code, iso, population, areaKm, gdp) = map[country.lower()]
            print("\nInfo for country {}"
                  "\n\tDialing Code : {}"
                  "\n\tPopulation   : {}"
                  "\n\tISO code     : {}"
                  "\n\tArea (KM)    : {}"
                  "\n\tGDP          : {}".format(name, code, population, iso, areaKm, gdp))
        else:
            print("Hey, bell-end - I haven't a clue what {} is!".format(country))
        country = str(raw_input("Want to go again then type in another bleeding country name or 'fuck off'...>> "))

