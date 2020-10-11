import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.config import *

def send_mail(report_file):
    """编写邮件内容"""
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file,encoding="utf-8").read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    """组装Email头(发件人,收件人,主题)"""
    msg['From'] = sender
    msg["To"] = receiver
    msg['Subject'] = Header(subject,"utf8")


    """构造附件,传送当前目录下的test.txt文件"""
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    """连接smtp服务器并发送邮件"""
    try:
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_password)
        smtp.sendmail(*receiver,msg.as_string())
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()