#!/usr/bin/python
from ip_renew import *
from bs4 import BeautifulSoup


for i in range(0,2):
    renew_connection()
    #print request("http://icanhazip.com/")
    #print request("http://xmh57jrzrnw6insl.onion")
    #print request("http://2222ppclgy2amp23.onion/")
    #url = "http://xmh57jrzrnw6insl.onion"
    url = "http://rrcc5uuudhh4oz3c.onion/"
    print request(url)
    r = request(url)
    soup = BeautifulSoup(r)
    found = soup.findAll("a",{"style": "font-weight:bold;"})[0].string
    print found


'''def make_request():
    r = request(url)
    data = r.text
    soup = BeautifulSoup(data)
    for link in soup.find_all('a'):
        print(link.get('href'))

make_request'''
