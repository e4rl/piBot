# !/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

my_sender = 'x@qq.com'
my_pass = 'x'
my_user = 'x@qq.com'


def mail():
    ret = True
    try:
        msgRoot = MIMEMultipart('related')
        msgRoot['From'] = formataddr(["Robot",my_sender])
        msgRoot['To'] = formataddr(["E4rl",my_user])
        subject = '请扫码登录'
        msgRoot['Subject'] = Header(subject, 'utf-8')

        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        mail_msg = """
        <img src="cid:image1">
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

        fp = open('temp/wxqr.png', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()

        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, [my_user, ], msgRoot.as_string())
        server.quit()
    except Exception:
        ret = False
    return ret

def send():
    ret = mail()
    if ret:
        print("[INFO] Mail sent successfully")
    else:
        print("[INFO] Mail delivery failed")
