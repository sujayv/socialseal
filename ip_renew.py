#!/usr/bin/python
from TorCtl import TorCtl
import urllib2
import urllib

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
#headers={'User-Agent':user_agent,'Cookie':'PHPSESSID=377nje1uil206okervak02kti7; __utma=157815014.692379856.1476755824.1476755824.1476755824.1; __utmb=157815014.3.10.1476755824; __utmc=157815014; __utmz=157815014.1476755824.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
headers={'User-Agent':user_agent}


def _set_urlproxy():
    proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:8118"})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)

def requestget(url):
    _set_urlproxy()
    requesturl=urllib2.Request(url, None, headers)
    return urllib2.urlopen(requesturl)

def requestpost(url,cookie):
    _set_urlproxy()
    #headernew = {'Cookie':cookie,'Content-Type':'application/x-www-form-urlencoded','Content-Length':20}
    headernew = {'Cookie':'PHPSESSID=t1j818772529tq5bme5opkoal1'}
    headernew.update(headers)
    #print headernew
    #dict = {'agree':'Yes, I agree'}
    #encoded = urllib.urlencode(dict)
    #print encoded
    requesturl=urllib2.Request(url,None,headernew)
    return urllib2.urlopen(requesturl)

def requestgetnew(url,cookie):
    _set_urlproxy()
    headernew = {'Cookie':cookie}
    headernew.update(headers)
    #print headernew
    requesturl=urllib2.Request(url, "", headernew)
    return urllib2.urlopen(requesturl)

def renew_connection():
    conn = TorCtl.connect(controlAddr="127.0.0.1", controlPort=9051, passphrase="your_password")
    conn.send_signal("NEWNYM")
    conn.close()
