#!/usr/bin/python
from ip_renew import *
from bs4 import BeautifulSoup
import re

renew_connection()
url = "http://mvfjfugdwgc5uwho.onion/author/"
authornodes = {}
for i in range(1,10):
	forum = requestpost(url+(str)(i),"")
	soup = BeautifulSoup(forum.read(),'lxml')
	#print soup
	####For author name######
	authornametag = soup.find_all('div',class_='category_title')
	m = re.search('Author: (.*)<\/a>',str(authornametag))
	authorurl = m.group(0)
	print "\n"
	anchortagindex = authorurl.index("</a>")
	authorname = authorurl[8:anchortagindex]
	######For author details
	authordetails = soup.find_all('div',class_='user_table_content')
	table = {}
	for details in authordetails:
		detailsoup = BeautifulSoup("<html>"+str(details)+"</html>","lxml")
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
	exploitdetails = soup.find_all('div',class_='ExploitTableContent')
#####Printing the author description table####
"""for key in authornodes.keys():
	print "***********************"
	temp = authornodes.get(key)
	print 'Author '+ str(key)
	for value in temp.keys():
		print value + " : \t" + str(temp.get(value))"""