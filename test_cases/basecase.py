import unittest

import pytest
import requests
import json
from lib.read_excel import *

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpclass(cls,data_file):
        if cls.__name__ != "BaseCase":
            cls.data_list = read_excel_data(data_file,cls.__name__)

    def get_case_data(self,case_name):
        return read_excel_data(self.data_list, case_name)

    @pytest.mark.usefixtures("log_case_info")
    def send_request(self,case_data):
        self.case_name = case_data.get('case_name')
        self.url = case_data.get('url')
        self.args = case_data.get('args')
        self.headers = case_data.get('headers')
        self.expect_res = case_data.get('expect_res')
        self.method = case_data.get('method')
        self.data_type = case_data.get('data_type')

        if self.method.upper() == "GET":
            self.res = requests.get(url=self.url,params=json.loads(self.args))
        elif self.data_type.upper() == "FROM":
            self.res = requests.post(url=self.url,data=json.loads(self.args),headers=json.loads(self.headers))
            assert self.res.text == self.expect_res
        else:
            self.res = requests.post(url=self.url,json=json.loads(self.args),headers=json.loads(self.headers))
            assert self.res.json() is json.loads(self.expect_res)