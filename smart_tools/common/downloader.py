import requests

def get_url(url, http_proxy ='http://proxy:8080', https_proxy ='http://username:pwd@proxy:8080'):
    proxy = {}

    if http_proxy:
        proxy['http'] = http_proxy
    if https_proxy:
        proxy['https'] = https_proxy

    return requests.get(url, proxy)

def download_url(url, filename, encoding ='utf-8', http_proxy ='http://proxy:8080', https_proxy ='http://username:pwd@proxy:8080'):
    response = get_url(url, http_proxy, https_proxy)

    with open(filename, 'wb') as f:
        f.write(response.content)
    return f
