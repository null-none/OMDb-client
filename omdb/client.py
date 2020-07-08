import requests, json


class OMDAPI(object):

    def __init__(self, key, type='movie', plot='full', r='json'):
        self.key = key
        self.url = 'http://www.omdbapi.com/?apikey={0}&'.format(key)
        self.type = type # movie, series, episode
        self.plot = plot # short, full
        self.r = 'json' # json, xml


    def search_title(self, t='', y=''):
        url = '{}t={}&y={}'.format(self.url, t, y)
        result = requests.get(url)
        return result.json()

    def search_id(self, i):
        url = '{}i={}'.format(self.url, i)
        result = requests.get(url)
        return result.json()