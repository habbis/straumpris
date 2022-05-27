#!bin/python3

from urllib import response
import requests
from bs4 import BeautifulSoup

electricity_rates_link = "https://www.finnas-kraftlag.no/produkt-og-prisinformasjon/category1445.html"


response = requests.get(electricity_rates_link)

soup = BeautifulSoup(response.text, 'html.parser')


electricity_rates_info = soup.findAll('div', attrs={"class":"grid-item"})

for electricity_rates in electricity_rates_info:
    print(electricity_rates.text)