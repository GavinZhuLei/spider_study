import urllib2
import re


def set_proxy(ip):
    """
    设置代理
    """
    proxy_support = urllib2.ProxyHandler({'http': ip})
    opener = urllib2.build_opener(proxy_support)
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')]

    urllib2.install_opener(opener)


def get_iplist():
    """
    获取最新的ip地址服务器
    """
    url = 'http://cn-proxy.com'

    try:
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36')
        response = urllib2.urlopen(req)
    except:
        set_proxy('27.202.2.136:80')
        req = urlllib2.Request(url)
        response = urllib2.urlopen(req)
        
    html = response.read().decode('utf-8')

    list_tr = re.findall(r'<tr>.+?</tr>', html, re.S)
    list_ip = []
    for tr in list_tr:
        ip_td = re.findall(r'<td>.+?</td>', tr, re.S)
        if len(ip_td):
            ip = re.search(r'((?:(?:25[0-5]|2[0-4]\d|[01]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d?\d))', ip_td[0])
            if ip:
                port = re.search(r'[0-9]{1,5}', ip_td[1])
                list_ip.append(ip.group(0)+':'+port.group(0))

    return list_ip
        
    

if __name__ == "__main__":
    ips = get_iplist()
    for ip in ips:
        print ip
