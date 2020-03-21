#  ▄▄ • ▄ •▄      ▄▄▄·▄▄▄  ▄▄▄ .• ▌ ▄ ·. ▪  ▄• ▄▌• ▌ ▄ ·.     .▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄·▪   ▐ ▄  ▄▄ •
# ▐█ ▀ ▪█▌▄▌▪    ▐█ ▄█▀▄ █·▀▄.▀··██ ▐███▪██ █▪██▌·██ ▐███▪    ▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄███ •█▌▐█▐█ ▀ ▪
# ▄█ ▀█▄▐▀▀▄·     ██▀·▐▀▀▄ ▐▀▀▪▄▐█ ▌▐▌▐█·▐█·█▌▐█▌▐█ ▌▐▌▐█·    ▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀·▐█·▐█▐▐▌▄█ ▀█▄
# ▐█▄▪▐█▐█.█▌    ▐█▪·•▐█•█▌▐█▄▄▌██ ██▌▐█▌▐█▌▐█▄█▌██ ██▌▐█▌    ▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█▌██▐█▌▐█▄▪▐█
# ·▀▀▀▀ ·▀  ▀    .▀   .▀  ▀ ▀▀▀ ▀▀  █▪▀▀▀▀▀▀ ▀▀▀ ▀▀  █▪▀▀▀     ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀   ▀▀▀▀▀ █▪·▀▀▀▀

# Author :
# +-+-+-+-+-+-+-+-+-+
# |I|A|m|T|e|r|r|o|r|
# +-+-+-+-+-+-+-+-+-+

# Licence :
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  0. You just DO WHAT THE FUCK YOU WANT TO.

# Notes :
# Python script tested on Ubuntu Linux. It can run on Windows with minor adjustements.


########################################################################################################################

########################################################################################################################

# !/usr/bin/python
# -*- coding: utf-8 -*-

from credentials import *
import requests
from bs4 import BeautifulSoup

# VARIABLES ------------------------------------------------------------------------------------------------------------

url_premium_base = "https://www.gamekult.com/mon-compte/mes-codes-premium.html"
LIMIT = 14


# FUNCTIONS ------------------------------------------------------------------------------------------------------------

# my credentials, my choices
def payload(username, password):
    # start the session
    session = requests.Session()
    # create the payload
    payload = {'_username': username,
               '_password': password
               }
    # post the payload to the site to log in
    session.post("https://www.gamekult.com/utilisateur/connexion.html", data=payload)
    return session


# FIX : Replace for manual limit
# def limit_urls(session):
#     urls_to_scrapping = []
#     count = 1
#     is_in_bounds = True
#     while is_in_bounds:
#         r = session.get(url_premium_base + "?page=" + str(count))
#         if r.status_code == 200:
#             urls_to_scrapping.append(r.url)
#             count += 1
#             print(count)
#         else:
#             is_in_bounds = False
#     return urls_to_scrapping

def limit_urls():
    urls_to_scrapping = []
    count = 1
    for i in range(0, LIMIT):
        urls_to_scrapping.append(url_premium_base + "?page=" + str(count))
        count += 1
    return urls_to_scrapping


# cooking of a delicious soup with Beautiful Soup
def soup_cooking(session, url):
    # navigate to the next page and scrape the data
    page = session.get(url)
    # cook the soup
    a_delicious_soup = BeautifulSoup(page.text, 'html.parser')
    return a_delicious_soup


# creation of a dictionary of codes items with theirs titles and links
def get_code_items_with_theirs_titles_and_links(soup):
    global child
    dictionary_of_codes_items_with_theirs_titles_and_links = {}
    # get code items
    pm_offer_container = soup.find_all('aside', {'class': 'pm__offer__container'})
    for elem in pm_offer_container:
        children = elem.findChildren("span", recursive=False)
        for child in children:
            dictionary_of_codes_items_with_theirs_titles_and_links[child.contents[0]] = []
        # get titles
        pm_premium_h_lg = elem.parent.parent
        title = pm_premium_h_lg.contents[3].h4.contents[1].string
        # get links
        link = pm_premium_h_lg.contents[3].h4.contents[1].get('href')
        dictionary_of_codes_items_with_theirs_titles_and_links[child.contents[0]] = [title, link]
    return dictionary_of_codes_items_with_theirs_titles_and_links


# SCRIPT ---------------------------------------------------------------------------------------------------------------

# create the session with authentification
session = payload(USERNAME, PASSWORD)

# cook the soup
soup = soup_cooking(session, url_premium_base)

# get all datas
datas = get_code_items_with_theirs_titles_and_links(soup)

# test = limit_urls()
# print(test)

# TODO : multi URL
# TODO optionnel : limite dynamique
# TODO : gérer les codes déjà utilisés

