import pytest
from data_object.account import Account
from helper.api.account_helper import AccountHelper
import allure


@allure.parent_suite('API Test')
@allure.suite('Test Login')
class TestLogin:
    @allure.title('Test login with valid account')
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json', 'valid'))
    def test_login_successfully_with_valid_account(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 200
        assert response.json()["email"] == account.email
        assert response.json()["localId"] == account.user_id

    @allure.title('Test login with blank email')
    @pytest.mark.parametrize("account",
                             Account.get_list_account_from_json('resources/test_data/account.json', 'blank_email'))
    def test_login_unsuccessfully_with_blank_email(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 400
        assert response.json()["error"]["message"] == 'INVALID_EMAIL'

    @allure.title('Test login with blank password')
    @pytest.mark.parametrize("account",
                             Account.get_list_account_from_json('resources/test_data/account.json', 'blank_password'))
    def test_login_unsuccessfully_with_blank_password(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 400
        assert response.json()["error"]["message"] == 'MISSING_PASSWORD'

    @allure.title('Test login with invalid email')
    @pytest.mark.parametrize("account",
                             Account.get_list_account_from_json('resources/test_data/account.json', 'invalid_email'))
    def test_login_unsuccessfully_with_invalid_email(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 400
        assert response.json()["error"]["message"] == 'EMAIL_NOT_FOUND'

    @allure.title('Test login with invalid email format')
    @pytest.mark.parametrize("account",
                             Account.get_list_account_from_json('resources/test_data/account.json', 'invalid_email_format'))
    def test_login_unsuccessfully_with_invalid_email_format(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 400
        assert response.json()["error"]["message"] == 'INVALID_EMAIL'

    @allure.title('Test login with invalid password')
    @pytest.mark.parametrize("account",
                             Account.get_list_account_from_json('resources/test_data/account.json', 'invalid_password'))
    def test_login_unsuccessfully_with_invalid_password(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 400
        assert response.json()["error"]["message"] == 'INVALID_PASSWORD'