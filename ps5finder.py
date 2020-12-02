#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import os.path
import sys
import time
import argparse
import requests
from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

def request_text_exists(url, tlist):
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox") # linux only
    chrome_options.add_argument("--headless")
    try:
       chrome_options.headless = True
    except AttributeError:
        pass
    browser = webdriver.Chrome(options=chrome_options)
    #browser = Firefox(executable_path="/usr/local/bin/geckodriver", options=options)

    browser.get(url)
    html = browser.page_source #.encode("utf-8")
    browser.quit()

    for t in tlist:
        if t in html:
            return True

    #soup = BeautifulSoup(html, 'html5lib')
    #for t in tlist:
    #    print(soup(text=t))

    #print(soup.prettify())

    #if text in result:
    #    return True
    #return False
    #nav = browser.find_element_by_id("sony-text-body-1")
    #print(nav)

    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store', dest='refresh',
                        default='60',
                        help='refresh time in seconds')

    results = parser.parse_args()

    refresh = results.refresh

    psdirect_digital_url = "https://direct.playstation.com/en-us/consoles/console/playstation5-digital-edition-console.3005817"
    if request_text_exists(psdirect_digital_url, ["<p class=\"sony-text-body-1\">Out of Stock</p>", "We’re experiencing very high traffic."]):
        print("out of stock")

