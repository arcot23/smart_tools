import requests

def geturl(url, useproxy = False, proxy = 'proxy:8080', userid = "proxyuser", pwd = "proxypwd"):
    """
    Get content of a url.
    :param url: URL to get content from.
    :param useproxy: Set to True if request to a URL must be made through a proxy.
    :param proxy: If `useproxy` is True, then the proxy address. Do not include http:// or https://, just the address.
    :param userid: If `useproxy` is True, then  userid for secured request.
    :param pwd: If `useproxy` is True, then  password for secured request.
    :return: Content of the URL.
    """
    if useproxy:
        p = {'proxy': {'http': f'http://{proxy}', 'https': f'https://{userid}:{pwd}@{proxy}'}}
        return requests.get(url, proxies=p)
    return requests.get(url)


r = geturl(r'https://ofac.treasury.gov/faqs/topic/1641')

print(r)