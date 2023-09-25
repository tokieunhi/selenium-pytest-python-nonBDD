import json

import requests


class BaseAPI:

    def __init__(self, url, headers=None, data=None, params=None):
        self._url = url
        self._headers = headers
        self._data = data
        self._params = params

    @classmethod
    def get_default_header(cls, token):
        return {'Authorization': 'Bearer ' + token,
                'Content-Type': 'application/json'}

    @classmethod
    def get_referer_header(cls, api_url):
        return {'Referer': api_url}

    def get(self):
        return requests.get(self._url)

    def post(self):
        return requests.post(self._url, headers=self._headers, data=self._data, params=self._params)

    def put(self):
        return requests.put(self._url, headers=self._headers, data=self._data, params=self._params)

    def delete(self):
        return requests.delete(self._url, headers=self._headers, data=self._data, params=self._params)
