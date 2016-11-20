#!/usr/bin/python
from ip_renew import *
from bs4 import BeautifulSoup
import re
from py2neo import authenticate, Graph, Path, Node, Relationship
#from dbconnect import *

authenticate("localhost:7474", "neo4j","password")
graph = Graph("http://localhost:7474/db/data")
labels = graph.node_labels

website_name = "Oday-test"
website_node = Node("Website", name=website_name)

graph.merge(website_node)

renew_connection()
url = "http://mvfjfugdwgc5uwho.onion/author/"
authornodes = {}
authortopics = {}
for i in range(0,3):
	forum = requestpost(url+(str)(i),"")
	soup = BeautifulSoup(forum.read(),'lxml')
	#print soup
	####For author name######
	authornametag = soup.find_all('div',class_='category_title')
	m = re.search('Author: (.*)<\/a>',str(authornametag))
	authorurl = m.group(0)
	#print "\n"
	anchortagindex = authorurl.index("</a>")
	authorname = authorurl[8:anchortagindex]
	######For author details
	authordetails = soup.find_all('div',class_='user_table_content')
	table = {}
	for details in authordetails:
		detailsoup = BeautifulSoup("<html>"+str(details)+"</html>","lxml")
		field = detailsoup.find_all('div',class_='td')
		#print field[0].string
		if(field[0].string == 'Author'):
			tp = detailsoup.find_all('a')
			#print tp[0].string
			node = {field[0].string:tp[0].string}
			table.update(node)
		else:
			#print field[1].string
			node = {field[0].string : field[1].string}
			table.update(node)
	finaltable = {i:table}
	authornodes.update(finaltable)
	#print soup
	m1 = re.search('<div class="pages">(.*?)<\/div>',str(soup))
	lastpagenumber = 1
	if(m1 != None):
		pagessoup = BeautifulSoup("<html>"+str(m1.group(0))+"</html>","lxml")
		pagetags = pagessoup.find_all('a')
		for tag in pagetags:
			#print tag.string
			if(tag.string.isnumeric()):
				if(int(tag.string) > lastpagenumber):
					lastpagenumber = int(tag.string)
	#print 'The last page is '+ str(lastpagenumber)
	topicnamelist = {}
	for j in range(1,lastpagenumber+1):
		page = requestpost(url+(str)(i)+"/"+str(j),"")
		pagesoup = BeautifulSoup(page.read(),'lxml')
		exploitdetails = pagesoup.find_all('div',class_='ExploitTableContent')
		for details in exploitdetails:
			#print '***********************************'
			exploit = BeautifulSoup("<html>"+str(details)+"</html>","lxml")
			#print exploit
			exploitname = exploit.find_all('div',class_='td allow_tip ')
			#print exploitname
			exploitnamesoup = BeautifulSoup("<html>"+str(exploitname[0])+"</html>",'lxml')
			topic = exploitnamesoup.find_all('a')
			topicname = topic[0].string
			#print topicname
			platforms = exploit.find_all('div',class_='td')
			#print platforms
			platformsoup = BeautifulSoup("<html>"+str(platforms[2])+"</html>",'lxml')
			#print platformsoup
			platformatags = platformsoup.find_all('a')
			#print "The a tag is "
			#print platformatags
			platformname = "unsorted"
			if len(platformatags) != 0:
				platformname = platformatags[0].string
			#print platformname
			temptopicpair = {topicname:platformname}
			topicnamelist.update(temptopicpair)
	topickeyvalue = {i:topicnamelist}
	authortopics.update(topickeyvalue)



#####Printing the author description table####
#file = open("output.txt","a")
template = "{0:70}:{1:10}"
templateauthor = "{0:15}:{1:20}"
for key in authornodes.keys():
	print "***********************"
	authors = authornodes.get(key)
	#print 'Author '+ str(key)
	#print value + " : \t" + str(temp.get(value))
	author_name = str(authors.get("Author"))
	author_node = Node("author",name=author_name,BL=str(authors.get("BL")),Readers=str(authors.get("Readers")),Exploits=str(authors.get("Exploits")),Registration_date=str(authors.get("Reg date")))
	graph.merge(author_node)
	graph.create(Relationship(website_node,"has_author",author_node))
	#file.write("***************************************\n")
	#authors = authornodes.get(key)
	topic = authortopics.get(key)
	#print str(topic.get("Platform"))
	#file.write('Author '+ str(key) + "\n")
	#for value in authors.keys():
		#print value + " : \t" + str(authors.get(value))
		#file.write(templateauthor.format(value,authors.get(value))+"\n")
	#print "Topics:"
	#print "Name \t" + "Platform"
	#file.write(template.format("Topics","Platform")+"\n")
	for name1 in topic.keys():
		#print topic.get(name)
		print "**********************"
		topic_node = Node("topic",name=topic.get(name1))
		print topic_node
		graph.create(topic_node)
		graph.create(Relationship(author_node,"talks_about",topic_node))
		#file.write(template.format(name,topic.get(name))+"\n")'''
