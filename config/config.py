import logging
import os
import time

today = time.strftime('%Y%m%d',time.localtime())

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = os.path.join(prj_path, "log",f"{today}log.txt")
test_data_file = os.path.join(prj_path, "test_data")
report_file = os.path.join(prj_path, "report",f"{today}test_api_report.html")

logging.basicConfig(level=logging.DEBUG,
                    format="[%(asctime)s] %(levelname)s [%(funcName)s:%(filename)s, %(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    filemode="a")


"""数据库配置"""
db_host = '192.168.66.91'
db_port = 3306
db_user = 'testuser'
db_passwd = '1234567'
db = 'ai_test'

"""邮件配置"""
smtp_server = 'https://mail.163.com'
smtp_user = '18268878747@163.com'
smtp_password = 'huxiao694992104'

sender = smtp_user  # 发件人
receiver = ('1693153547@qq.com',"18267835018@163.com")   # 收件人
subject = '接口测试运行报告'  # 邮件主题

# if __name__ == "__main__":
#     logging.info("hello")