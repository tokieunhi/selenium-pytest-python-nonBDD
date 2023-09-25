import requests
from core.api.request_helper import BaseAPI
from core.env_info.env_info import EnvironmentInfo
import json

class BookHelper():
    book_api_category = '/BookStore/v1/'
    add_book_endpoint = book_api_category + 'Books'
    delete_book_endpoint = book_api_category + 'Book'

    @classmethod
    def add_a_book_to_collection(cls, token, user_id, isbn):
        data = json.dumps({
            "userId": user_id,
            "collectionOfIsbns": [
            {
                "isbn": isbn
            }]
        })

        headers = BaseAPI.get_default_header(token)
        return BaseAPI(url=EnvironmentInfo.api_url + cls.add_book_endpoint, data=data, headers=headers).post()
    
    @classmethod
    def delete_a_book_from_collection(cls, token, user_id, isbn):
        data = json.dumps({
            "isbn": isbn,
            "userId": user_id
        })
        headers = BaseAPI.get_default_header(token)
        return BaseAPI(url=EnvironmentInfo.api_url + cls.delete_book_endpoint, data=data, headers=headers).delete()