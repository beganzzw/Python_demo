from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

# 网易邮箱的垃圾邮件匹配规则有问题
# 现在修改成用QQ邮箱的邮件发送
def main():
    sender = '504699272@qq.com'  
    receivers = '18818037397@163.com'
    subject = ''
    message = MIMEText('hello','plain','utf-8')
    message['From'] = Header(sender,'utf-8')
    message['to'] = Header(receivers,'utf-8')
    message['Subject'] = Header(subject,'utf-8')
    smtper = SMTP('smtp.qq.com')
    smtper.login(sender,'dczhvsekrzyybgif')
    smtper.sendmail(sender,receivers,message.as_string())
    print('邮件发送完成!')

if __name__ == '__main__':
    main()