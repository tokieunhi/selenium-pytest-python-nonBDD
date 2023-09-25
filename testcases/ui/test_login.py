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

from page_object.home_page import HomePage
from page_object.popup.sign_in_form import SignInForm


@allure.parent_suite('UI Test')
@allure.suite('Test Delete Book')
class TestDeleteBook():
    @allure.title("Test delete a valid book")
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json', 'valid'))
    def test_login_successfully_with_valid_account_ui(self, account):

        Report.report_step('Go to Sign in form')
        home_page = HomePage()
        home_page.go_to_login_form()

        Report.report_step('Enter email')
        sign_in_form = SignInForm()
        sign_in_form.enter_email(account.email)

        Report.report_step('Enter password')
        sign_in_form.enter_password(account.password)

        Report.report_step('Click Sign In button')
        sign_in_form.click_sign_in_btn()

        Report.report_step('Verify login successfully')
        profile_page = ProfilePage()
        assert profile_page.is_email_displayed() == True

        # Report.report_step('Check book removed from the profile')
        # assert profile_page.does_book_exist(book.book_name) == False
