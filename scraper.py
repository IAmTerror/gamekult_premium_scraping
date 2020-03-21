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

url = "https://www.gamekult.com/mon-compte/mes-codes-premium.html"


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


# cooking of a delicious soup with Beautiful Soup
def soup_cooking(session, url):
    # navigate to the next page and scrape the data
    page = session.get(url)
    # cook the soup
    a_delicious_soup = BeautifulSoup(page.text, 'html.parser')
    return a_delicious_soup


# creation of a dictionary with file names and theirs associated fake urls
# def grab_titles_with_theirs(soup):


# SCRIPT ---------------------------------------------------------------------------------------------------------------
# create the session with authentification
session = payload(USERNAME, PASSWORD)

# cook the soup
soup = soup_cooking(session, url)
print(soup)