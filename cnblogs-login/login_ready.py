# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import cookielib
import urllib2
import urllib
import random


class BlogLogin(object):
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        self.input1 = self.input2 = self.remember = ''

        try:
            self.cj.revert('cnblogs.coockie')
        except Exception,e:
            print e
        self.iplist = ['116.236.203.238:8080', '119.187.113.217:81', '101.69.199.99:80']
        # proxy_support = urllib2.ProxyHandler({'http': random.choice(self.iplist)})
        # proxy_opener = urllib2.build_opener(proxy_support)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(opener)
        # urllib2.install_opener(proxy_opener)

    def save_cookie(self):
        req = ('http://passport.cnblogs.com/user/signin')
        html = self.opener.open(req).read()
        if self.cj:
            print self.cj
            self.cj.save('cnblogs.coockie')

    def login_page(self):
        print self.cj
        response = urllib2.urlopen('http://passport.cnblogs.com/user/signin')
        print response.read()
        print self.cj

    def set_login_info(self, input1, input2, remember):
        self.input1 = input1
        self.input2 = input2
        self.remember = remember

    def login(self):
        params = {'input1':self.input1,'input2':self.input2,'remember':self.remember}
        req = urllib2.Request(
            'http://passport.cnblogs.com/user/signin',
            urllib.urlencode(params),
        )
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
        req.add_header('VerificationToken','NLlOHafUOJRQkHr9wtB0N4bDF30EyrSPqJWqjpDv0tqLe1cnH2GVpeiDu-7wwJxhGAN8Oi4ZSwBq9jKMxrW-bY96phY1:YobqH0G3zDZU4S0D0NvWIp0Y5EVO4PHGnmLZ-mmyIMO7C0f1l4Pk5OWaSEnMb7DGbihwqbpi2o7yOMo-gC_3v1PSUqA1')
        req.add_header('X-Requested-With','XMLHttpRequest')

        response = urllib2.urlopen(req)
        print response.read()
        print self.cj
        # self.operate = self.opener.open(req)
        # # print self.operate.read()
        # print self.operate.geturl()


login = BlogLogin()
login.login_page()
# login.save_cookie()
login.set_login_info('cIbesOEA8F0hjYOiYAFmYhq+bMedHIpLudlnCYuXBQgZMoCxJAUPnXweO0jh5smtfuhuPciDMRCyhijsWhSNEgz113bgypk0XhD0p1dgxHI85Xii0sxRa2KaDEdHQSNYEF9lfYYvM/BONRHL52G1Vx+rsSfYwQ7PG/ofTbedjyE=',
                     'PjTozIwfOFjX5Bfi9B/UQlrOU3NdOaVrXhNL0rStTaSO683BtaIrSDgbrO67Fty0YA4XSOWodhI3IQ0aarvaW0SY58AVcHOc6y97c03asSplbpMMgPTxY0yupyJzGQ/Em/jKwSBql75XIhH23co4r6G6UJN6BnKrH5qOz19Mf3c=',
                     False)
login.login()





