#!/usr/bin/env python

"""
This is me learning Python...

https://countrycode.org/ provides a fantastic feature for phoning people anywhere across the world.
It gives you the calling chart to help you find the dialing codes you need to make long distance phone
calls to friends, family, and business partners around the globe. where by you can get information on a country.

So I thought it would be useful to pull out, in JSON format, each country and it's respective code, like the following:

            {
                "Afghanistan": "AF",
                "Albania": "AL",
                "Algeria": "DZ",
                "American Samoa": "AS",
                ...
                ...
                "Western Sahara": "EH",
                "Yemen": "YE",
                "Zambia": "ZM",
                "Zimbabwe": "ZW"
            }
"""

__author__ = "Kevin Orr"


# suck in the 'requests' module for doing http stuff - like pulling down the html
import requests
# for parsing the html we'll use BeautifulSoup
from bs4 import BeautifulSoup
# and for JSONifying the results
import json

# if you didn't want to use the 'requests' module you could use 'liburl' or 'liburl2' modules
# import urllib

# This function makes a call out to countrycode.org, pull down and parses the html containing the country codes
# and then finally build up a map of name/code.
def get_country_codes():
    map = dict()
    r = requests.get('https://countrycode.org/')
    soup = BeautifulSoup(r.text, 'html.parser')

    #
    # now if you didn't want to use 'requests' module you could use the 'urllib' module
    # instead and pass the response straight into the BeautifulSoup parser:
    # r = urllib.urlopen('https://countrycode.org/').read()
    # soup = BeautifulSoup(r, 'html.parser')
    #

    #  now lets pull out the table rows...
    rows = soup.table.tbody.find_all('tr')
    # and run over the collection of rows to get the country name and it's associated ISO code
    for row in rows:
        [country_name, _, iso_code, _, _, _] = row.find_all('td')
        map[country_name.text] = iso_code.text.split('/')[0].strip()

    return map


# return the JSON representation of country code map.
def get_country_code_in_json():
    map = get_country_codes()
    js = json.dumps(map, sort_keys=True, indent=4, separators=(',', ': '))
    return js


if __name__ == '__main__':
    # print out the json
    print(get_country_code_in_json())