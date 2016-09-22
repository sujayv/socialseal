#!/usr/bin/python
from ip_renew import *
from bs4 import BeautifulSoup
import re

for i in range(0,1):
    renew_connection()
    #print request("http://icanhazip.com/")
    #print request("http://xmh57jrzrnw6insl.onion")
    #print request("http://2222ppclgy2amp23.onion/")
    #url = "http://xmh57jrzrnw6insl.onion"
    url2 = "http://rrcc5uuudhh4oz3c.onion/"
    url = "http://rrcc5uuudhh4oz3c.onion/?cmd=category&id=12"
    #print request(url)
    r = request(url)
    soup = BeautifulSoup(r)
    #print soup.prettify()
    #found = soup.findAll("a",{"style": "font-weight:bold;"})[0].string
    for link in soup.findAll('a', href=True):
        print "Found URL is: %s"%link['href']
        print "For topic %s"%link.string
        #print link.string
    #found2 = soup.findAll("a",{"style": "font-weight:bold;"})[0].string
    #print found


'''def make_request():
    r = request(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

make_request'''
