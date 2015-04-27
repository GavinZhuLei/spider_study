# -*- coding: utf-8 -*-
# __author__ = 'Gavin'
import cookielib
import urllib2
import urllib
import random


class CNBlogsCookie(object):
    def __init__(self):
        self

class BlogLogin(object):
    def __init__(self):
        self.cj = cookielib.LWPCookieJar()
        # self.cj = cookielib.CookieJar()
        self.input1 = self.input2 = self.remember = ''

        cookie1 = cookielib.Cookie(name='.CNBlogsCookie',
                                  value='A55CC1F05099889A9F411F069D6BBA1868B05F66D13D91C656827FA69E40613BCBD05A2253E09DCF3555A9B84F664807A3945D1A8DC33E4B1E6C6D5A6086EB88763E23585CCD21C231548C0B44372692FBF05FEC',
                                  domain='.cnblogs.com',
                                  path='/',
                                  comment=None,
                                  version=None,
                                  secure=None,
                                  rest=None,
                                  port=None,
                                  expires=30*60,
                                  port_specified=None,
                                  domain_specified=None,
                                  domain_initial_dot=None,
                                  discard=None,
                                  comment_url=None,
                                  path_specified=None,
                                  )
        cookie2 = cookielib.Cookie(name='AspxAutoDetectCookieSupport',
                                  value='1',
                                  domain='passport.cnblogs.com',
                                  path='/',
                                  comment=None,
                                  version=None,
                                  secure=None,
                                  rest=None,
                                  port=None,
                                  expires=30*60,
                                  port_specified=None,
                                  domain_specified=None,
                                  domain_initial_dot=None,
                                  discard=None,
                                  comment_url=None,
                                  path_specified=None,
                                  )
        cookie3 = cookielib.Cookie(name='SERVERID',
                                  value='225b7d8360ba35c5a9afdd81703cfcc6|1430145223|1430145223',
                                  domain='passport.cnblogs.com',
                                  path='/',
                                  comment=None,
                                  version=None,
                                  secure=None,
                                  rest=None,
                                  port=None,
                                  expires=30*60,
                                  port_specified=None,
                                  domain_specified=None,
                                  domain_initial_dot=None,
                                  discard=None,
                                  comment_url=None,
                                  path_specified=None,
                                  )
        # self.cj.set_cookie(cookie1)
        # self.cj.set_cookie(cookie2)
        # self.cj.set_cookie(cookie3)

        # try:
        #     self.cj.revert('cnblogs.coockie')
        # except Exception,e:
        #     print e
        self.iplist = ['210.14.158.122:80', '119.136.34.135:80', '113.107.56.97:80']
        proxy_support = urllib2.ProxyHandler({'http': '119.187.113.217:81'})
        # proxy_opener = urllib2.build_opener(proxy_support)
        self.opener = urllib2.build_opener( urllib2.HTTPCookieProcessor())
        urllib2.install_opener(self.opener)
        # urllib2.install_opener(proxy_opener)

    def save_cookie(self):
        req = ('http://passport.cnblogs.com/user/signin')
        html = self.opener.open(req).read()
        if self.cj:
            print self.cj
            self.cj.save('cnblogs.coockie')

    def login_page(self):
        print self.cj
        response = self.opener.open('http://passport.cnblogs.com/user/signin')
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

        response = self.opener.open(req)
        print response.read()
        print self.cj
        # self.operate = self.opener.open(req)
        # # print self.operate.read()
        # print self.operate.geturl()

    def index_page(self):
        response = urllib2.urlopen('http://www.cnblogs.com')
        print response.read()

    def login_info(self):
        print self.cj
        req = urllib2.Request('http://passport.cnblogs.com/user/LoginInfo')
        # self.cj.add_cookie_header(req)

        self.cj.add_cookie_header(req)
        print req.has_header('Cookie')
        # req.add_unredirected_header('Cookie','.CNBlogsCookie=A55CC1F05099889A9F411F069D6BBA1868B05F66D13D91C656827FA69E40613BCBD05A2253E09DCF3555A9B84F664807A3945D1A8DC33E4B1E6C6D5A6086EB88763E23585CCD21C231548C0B44372692FBF05FEC')

        response = self.opener.open(req)
        print response.read()
        self.cj.save('cookie.txt')


login = BlogLogin()
login.login_page()
# login.save_cookie()
login.set_login_info('cIbesOEA8F0hjYOiYAFmYhq+bMedHIpLudlnCYuXBQgZMoCxJAUPnXweO0jh5smtfuhuPciDMRCyhijsWhSNEgz113bgypk0XhD0p1dgxHI85Xii0sxRa2KaDEdHQSNYEF9lfYYvM/BONRHL52G1Vx+rsSfYwQ7PG/ofTbedjyE=',
                     'PjTozIwfOFjX5Bfi9B/UQlrOU3NdOaVrXhNL0rStTaSO683BtaIrSDgbrO67Fty0YA4XSOWodhI3IQ0aarvaW0SY58AVcHOc6y97c03asSplbpMMgPTxY0yupyJzGQ/Em/jKwSBql75XIhH23co4r6G6UJN6BnKrH5qOz19Mf3c=',
                     False)
login.login()
# login.index_page()
# login.login_info()





