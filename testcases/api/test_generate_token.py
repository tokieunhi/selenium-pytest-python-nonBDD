import pytest
from data_object.account import Account
from helper.api.account_helper import AccountHelper
import allure

@allure.parent_suite('API Test')
@allure.suite('Test Generate Token')
class TestGenerateToken():
    @allure.title('Test generate token with a valid account')
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','valid'))
    def test_generate_token_successfully_with_valid_account(self, account):
        response = AccountHelper.generate_token(account)
        assert response.status_code == 200
        assert response.json()["token"] != None

    @allure.title('Test generate token with invalid accounts')
    @pytest.mark.parametrize("account", Account.get_list_account_from_json('resources/test_data/account.json','invalid'))
    def test_generate_token_unsuccessfully_with_invalid_account(self, account):
        response = AccountHelper.generate_token(account)
        assert response.json()["token"] == None