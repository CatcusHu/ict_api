import pytest
from lib.db import *
from test_cases.basecase import BaseCase

class TestUserLogin(BaseCase):
    def test_user_reg_normal(self):
        self.case_data = self.get_case_data("test_user_reg_normal")

        self.username = self.case_data.get("key")

        if check_user(self.username):
            del_user(self.username)

        self.send_request(self.case_data)

        assert self.res.status_code == 200
        assert check_user(self.username)

    def test_user_reg_exist(self):
        self.case_data = self.get_case_data("test_user_reg_exist")

        self.username = self.case_data.get("key")
        if not check_user(self.username):
            add_user(self.username)

        self.send_request(self.case_data)

if __name__ == "__main__":
    pytest.main(["-s","test_user_login.py"])