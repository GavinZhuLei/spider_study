import urllib2
import random

url = 'http://www.whatismyip.com.tw'

iplist = ['124.88.67.40:80', '183.131.144.204:80', '27.202.2.136:80']
##设置代理
proxy_support = urllib2.ProxyHandler({'http': random.choice(iplist)})
opener = urllib2.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')]

urllib2.install_opener(opener)

req = urllib2.Request(url)

response = urllib2.urlopen(req)
html = response.read()
print html
