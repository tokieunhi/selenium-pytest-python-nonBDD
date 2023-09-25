import pytest
from data_object.account import Account
from data_object.book import Book
from page_object.book_store_page import BookStorePage
from page_object.login_page import LoginPage
from page_object.profile_page import ProfilePage
from helper.api.book_helper import BookHelper
from helper.api.account_helper import AccountHelper
from core.report.allure_report import Report
from core.driver.driver_utils import DriverUtils
import allure

@allure.parent_suite('UI Test')
@allure.suite('Test Delete Book')
class TestDeleteBook():
    @allure.title("Test delete a valid book")
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','valid'))
    @pytest.mark.parametrize("book", Book.get_list_book_from_json('resources/test_data/book.json','valid'))
    def test_delete_book_with_ui(self, account, book):
        Report.report_step('Add a book to collection with API')
        BookHelper.add_a_book_to_collection(AccountHelper.get_token(account, True),account.user_id,  book.isbn)
        
        Report.report_step('Go to Log in page')
        book_store_page =  BookStorePage()
        book_store_page.go_to_login_page()
        
        Report.report_step('Log in to the application')
        login_page = LoginPage()
        login_page.login(account)
        
        Report.report_step('Go to profile page')
        book_store_page.wait_for_page_load()
        book_store_page.go_to_profile_page()
        
        Report.report_step('Delete book by name')
        profile_page = ProfilePage()
        profile_page.delete_book_by_name(book.book_name)
        
        Report.report_step('Check book removed from the profile')
        assert profile_page.does_book_exist(book.book_name) == False
