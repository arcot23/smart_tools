import requests

def geturl(url, useproxy = False, proxy = 'proxy:8080', userid = "proxyuser", pwd = "proxypwd"):
    if useproxy:
        p = {'proxy': {'http': f'http://{proxy}', 'https': f'https://{userid}:{pwd}@{proxy}'}}
        return requests.get(url, proxies=p)
    return requests.get(url)


r = geturl(r'https://ofac.treasury.gov/faqs/topic/1641')

print(r)