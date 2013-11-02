#import dns.resolver, dns.query, dns.zone
#import socket
import httplib 
from HTMLParser import HTMLParser 

# url = 'google.com'
# url_ip = socket.gethostbyname_ex(url)
# print url_ip

conn = httplib.HTTPConnection("python.org")
conn.request("GET", "/")
r1 = conn.getresponse()
# print r1.status, r1.reason 
data1 = r1.read()
headers = r1.getheaders()
# print headers
# print data1

class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print "Encountered a start tag:", tag
	def handle_endtag(self, tag):
		print "Encountered an end tag:", tag
	def handle_data(self, data):
		print "Encountered some data:", data

parser = MyHTMLParser()
parser.feed(data1)


#response = dns.resolver.query('url', 'MX')
#for rdata in response: 
#	print 'Host', rdata.exchange, 'has preference', rdata.preference

# zone = dns.zone.from_xfr(dns.query.xfr(('204.152.189.147'), 'dnspython.org'))
# names = zone.nodes.keys()
# names.sort()
# for n in names: 
# 	print zone[name].to_text(n)

# build the dom 

