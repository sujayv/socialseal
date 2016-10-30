#!/usr/bin/python
from ip_renew import *
from bs4 import BeautifulSoup
import re

renew_connection()
#print request("http://icanhazip.com/")
#print request("http://xmh57jrzrnw6insl.onion")
#print request("http://2222ppclgy2amp23.onion/")
#url = "http://xmh57jrzrnw6insl.onion"
url = "http://mvfjfugdwgc5uwho.onion/author/"
#url2 = "http://rrcc5uuudhh4oz3c.onion/"
#url = "http://rrcc5uuudhh4oz3c.onion/?cmd=category&id=12"
#print request(url)
#print website.read()
#print website.read()
#print website.geturl()
#cookie = website.info()['Set-Cookie']
#index = cookie.index(';')
#print cookie[0:index]
#dict = {'agree':'Yes, I agree'}
#encoded = urllib.urlencode(dict)<a href="/author/0">
#print url+'?'+encoded
authornodes = {}
for i in range(1,10):
	forum = requestpost(url+(str)(i),"")
	#forum = requestget(url)
	soup = BeautifulSoup(forum.read(),'lxml')
	#print soup
	####For author name######
	authornametag = soup.find_all('div',class_='category_title')
	#r = re.compile("Author: ")
	#print authornametag
	m = re.search('Author: (.*)<\/a>',str(authornametag))
	authorurl = m.group(0)
	print "\n"
	#print authorurl
	anchortagindex = authorurl.index("</a>")
	authorname = authorurl[8:anchortagindex]
	#print authorname
	######For author details
	authordetails = soup.find_all('div',class_='user_table_content')
	table = {}
	for details in authordetails:
		#print details
		detailsoup = BeautifulSoup("<html>"+str(details)+"</html>","lxml")
		#print detailsoup
		field = detailsoup.find_all('div',class_='td')
		print field[0].string
		if(field[0].string == 'Author'):
			tp = detailsoup.find_all('a')
			print tp[0].string
			node = {field[0].string:tp[0].string}
			table.update(node)
		else:
			print field[1].string
			node = {field[0].string : field[1].string}
			table.update(node)
	finaltable = {i:table}
	authornodes.update(finaltable)
for key in authornodes.keys():
	print "***********************"
	temp = authornodes.get(key)
	print 'Author '+ str(key)
	for value in temp.keys():
		print value + " : \t" + str(temp.get(value))
	#print soup.title.string
	#all_links=soup.find_all('a')
	#for link in all_links:
		#print link.get("href")
#print website.header_items()
#found = soup.findAll("a",{"style": "font-weight:bold;"})[0].string
#for link in soup.findAll('a', href=True):
#    #print "Found URL is: %s"%link['href']
#    print "For topic %s"%link.string
    #print link.string
#found2 = soup.findAll("a",{"style": "font-weight:bold;"})[0].string
#print found