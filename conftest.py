from config.config import *
import pytest
import json
from lib.send_email import send_mail


@pytest.fixture(scope="function")
def log_case_info(case_name,url,data,expect_res,res_text):
    if isinstance(data,dict):
        data = json.dumps(data,ensure_ascii=False)
    logging.info(f"测试用例：{case_name}")
    logging.info(f"url：{url}")
    logging.info(f"请求参数：{data}")
    logging.info(f"期望结果：{expect_res}")
    logging.info(f"实际结果：{res_text}")

def pytest_option(parser):
    parser.addoption("--runcase",action="store",default="")

if __name__=="__main__":
    pytest.main([f'--html="../{report_file}"','./test_cases'])
    send_mail(report_file)