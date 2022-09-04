#!env/bin/python3
"""
minimal python script
"""
import argparse
import os
from urllib import response
import requests
from bs4 import BeautifulSoup
#import pandas as pd
#import csv
#import re

electricity_rates_link = "https://www.finnas-kraftlag.no/produkt-og-prisinformasjon/category1445.html"

def main():
    #arg_parser  = argparse.ArgumentParser(description=__doc__)
    #arg_parser.add_argument("-n", "--name", help="desctription of the flag")

     # We parse the args here to do some additional
    # obscure checks
    #parsed_args = arg_parser.parse_args()
    #name     =  parsed_args.name

    response = requests.get(electricity_rates_link)

    soup = BeautifulSoup(response.text, 'html.parser')
    electricity_rates_info = soup.find_all('div', attrs={"class":"grid-item"})

    for electricity_rates_all in electricity_rates_info:
       print(electricity_rates_all.text)


  
    print (name)

if __name__ == "__main__":
    main()
