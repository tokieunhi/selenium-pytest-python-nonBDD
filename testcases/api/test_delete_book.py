from data_object.account import Account
from data_object.book import Book
from helper.api.book_helper import BookHelper
from helper.api.account_helper import AccountHelper
import pytest
import allure

@allure.parent_suite('API Test')
@allure.suite('Test Delete Book')
class TestDeleteBook():
    @allure.title('Test delete a valid book')
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','valid'))
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('resources/test_data/book.json','valid'))
    def test_delete_valid_book_successfully_with_api(self, account, book):
        token = AccountHelper.get_token(account)
        BookHelper.add_a_book_to_collection(token, account.user_id, book.isbn)
        response = BookHelper.delete_a_book_from_collection(token, account.user_id, book.isbn)
        assert response.status_code == 204

    @allure.title('Test delete invalid books')
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','valid'))
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('resources/test_data/book.json','invalid'))
    def test_delete_invalid_book_unsuccessfully_with_api(self, account, book):
        response = BookHelper.delete_a_book_from_collection(AccountHelper.get_token(account), account.user_id, book.isbn)
        error_message = response.json()["message"]
        assert response.status_code == 400
        assert error_message == 'ISBN supplied is not available in User\'s Collection!'
