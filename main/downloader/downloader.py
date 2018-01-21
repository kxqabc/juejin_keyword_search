import urllib.request


def download_json(url):
    if url is None:
        print('one invalid url is found!')
        return None
    response = urllib.request.urlopen(url)
    if response.getcode() != 200:
        print('response from %s is invalid!' % url)
        return None
    return response.read().decode('utf-8')

