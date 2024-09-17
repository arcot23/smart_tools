import requests

def request_url(url, http_proxy ='http://proxy:8080', https_proxy ='http://username:pwd@proxy:8080'):

    """
    Gets a Url and returns the `Response`.
    :param url: Url.
    :param http_proxy: Http proxy address if one is needed.
    :param https_proxy: Https proxy address if one is needed.
    :return: Response
    """
    proxy = {}

    if http_proxy:
        proxy['http'] = http_proxy
    if https_proxy:
        proxy['https'] = https_proxy

    return requests.get(url, proxies= proxy)

def download_url_to_file(url, filename, encoding = None, http_proxy = None, https_proxy = None):

    """
    Download content of the url to a file.
    :param url: Url.
    :param filename: Local filename to save the content to.
    :param encoding: Encoding of the `filename`. e.g., 'utf-8'
    :param http_proxy: Http proxy address if one is needed. e.g., 'http://proxy:8080'
    :param https_proxy: Https proxy address if one is needed. e.g., 'http://username:pwd@proxy:8080'
    :return: IO
    """
    response = request_url(url, http_proxy, https_proxy)

    with open(filename, 'wb', encoding=encoding) as f:
        f.write(response.content)
    return f
