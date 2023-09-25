import json

from core.api.request_helper import BaseAPI
from core.env_info.env_info import EnvironmentInfo


class AccountHelper:
    generate_token_endpoint = '/verifyPassword'
    global_token = None

    @classmethod
    def generate_token(cls, account):
        data = {
            "email": account.email,
            "password": account.password,
            "returnSecureToken": True
        }
        header = BaseAPI.get_referer_header(EnvironmentInfo.api_url)
        params = {'key': EnvironmentInfo.api_key}
        return BaseAPI(url=EnvironmentInfo.firebase_uri + cls.generate_token_endpoint, data=data,
                       headers=header, params=params).post()

    @classmethod
    def get_token(cls, account, re_generate=False):
        if cls.global_token == None or re_generate:
            cls.global_token = cls.generate_token(account).json()["idToken"]
        return cls.global_token
