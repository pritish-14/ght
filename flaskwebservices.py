import urllib2,json

url = 'http://127.0.0.1:5000/'

req = urllib2.Request(url)
req.add_header('Content-Type','application/json')

response = urllib2.urlopen(req)
