from core.utilities.file_utils import get_full_path
import json
class Book():
    def __init__(self, isbn, book_name):
        self.isbn = isbn
        self.book_name = book_name
    
    @classmethod
    def get_list_book_from_json(cls, json_file_path, book_type):
        result = []
        with open(get_full_path(json_file_path)) as f:
            data = json.load(f)
            list_json_book = data[book_type]
            for json_book in list_json_book:
                result.append(Book(**json_book))
            
        return result

