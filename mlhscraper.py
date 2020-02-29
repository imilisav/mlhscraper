"""
--------------------
mlhWebCrawler.py
--------------------
"""

####### IMPORTS
import requests
import sys
import csv
import numpy as np
from bs4 import BeautifulSoup

####### CONSTANTS
MLH_LINK = "https://mlh.io/seasons/na-2020/events"

####### GLOBALS
save_hackathons_to_csv = False # Saves all hackathon links to csv file.

####### GET MLH PAGE FOR NORTH AMERICAN HACKATHONS
mlhPage = requests.get(MLH_LINK)

####### CHECK STATUS CODE OF REQUEST
if mlhPage.status_code is not 200:
    print(mlhPage.status_code)
    sys.exit()

####### USE BEAUTIFULSOUP TO FIND ALL HACKATHONS IN HTML
names = ['Hackathon Name']
links = ['Hackathon URL']
soup = BeautifulSoup(mlhPage.content, 'html.parser')

for a in soup.find_all('a', class_='event-link', href=True):
    names.append()
    # go through each website, pulling sponsor links
    hackathonPage = requests.get(a['href'])
    if hackathonPage.status_code is not 200:
        print(a['href'] + " Could not be accessed.")
    else:
        hackathonSoup = BeautifulSoup(hackathonPage.content, 'html.parser')
        for child in hackathonSoup.find_all('section', class_='sponsor'):
            print(child)