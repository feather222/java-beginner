#python发送邮件和短信
#region
import os  #读取环境变量中的密钥，避免凭据泄露到GitHub
import smtplib  #建立网络，发送数据
from email.header import Header #设置邮件标题
from email.mime.multipart import MIMEMultipart  #创建邮件对象
from email.mime.text import MIMEText    #创建邮件正文
email = MIMEMultipart() 
email['From'] = '151343@163.com'
email['to'] = 'qae@qq.com， 123@qq.com'    #多个接收邮箱，用；分割
email['Subject'] = Header('Python邮件测试', 'utf-8')
#添加正文
text = 'Python学习ing'
#定义一个多行字母串作为邮件正文,'plain'表示纯文本,还有html邮件，'utf-8'表示编码格式
email.attach(MIMEText(text, 'plain', 'utf-8'))
#链接服务器并登录
smtp_obj = smtplib.SMTP('smtp.163.com', 25)   #163邮箱服务器地址和端口号
smtp_obj.login('151343@163.com', os.environ.get('MAIL_AUTH_CODE', ''))  #授权码从环境变量读取，请勿硬编码
#发送邮件
smtp_obj.sendmail('151343@163.com', 
                  ['qae@qq.com', '123@qq.com'], 
                  email.as_string()
                  )
#email.as_string(),将邮件对象转换为字符串发送
print('邮件发送成功')
#endregion
#如何发送带附件的邮件
#region
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib import quote    #处理文件中的特殊字符
email = MIMEMultipart()
email['From'] = '151343@163.com'
email['to'] = 'qae@qq.com'
email['Subject'] = Header('Python邮件测试', 'utf-8')
content = """<p>金纳米数据：</p>
<p>附件为金纳米数据，请查收!</p>
<br>
<p>祝，好！<p>
<hr>
<p>林志颖 即日</p>"""
email.attach(MIMEText(content, 'html', 'utf-8'))    #attach()方法添加邮件正文
with open('金纳米数据.txt', 'rb') as file:    #以二进制方式打开文件
    attachment = MIMEText(file.read(), 'base64', 'utf-8')
    attachment['content-type'] = 'application/octet-stream'  #设置附件类型为二进制流
    filename = quote('金纳米数据.txt')    #处理文件名中的特殊字符
    attachment['content-disposition'] = f'attachment;filename = "{filename}"'
email.attach(attachment)    #attach()方法添加附件
smtp_obj = smtplib.SMTP_SSL('smtp.163.com', 465)    #163邮箱服务器地址和端口号
smtp_obj.login('151343@163.com', os.environ.get('MAIL_AUTH_CODE', ''))  #授权码从环境变量读取，请勿硬编码
smtp_obj.sendmail('qae@qq.com','123@qq.com', 
                  email.as_string())
#endregion
#使用已封装函数进行发送邮件
#region
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote
EMAIL_HOST = 'smtp.162.com'
EMAIL_PORT = 465
EMAIL_USER = '1234@126.com'
EMAIL_AUTH = '123456'
def send_email(*, 
               from_user,
               to_user,
               suject = '',
               content = '',
               filenames = []):
    email = MIMEMultipart()
    email['From'] = from_user
    email['To'] = to_users
    email['Subject'] = Header(subject, 'utf-8')
    message = MIMEText(content, 'plain', 'utf-8')
    email.attach(message)
    for filename in filenames:
        with open(filename, 'rb') as file:
            #查找文件路径最后一个'/'的位置，获取文件名
            pos = filename.rfind('/') #反向寻找，实质上是寻找最后一个'/'的位置
            display_filename = filename[pos+1:] if pos >= 0 else filename
            #pos+1是为了1去除路径中的'/'，如果没有'/'，（实质上是取（/到-1））则直接使用filename
            display_filename = quote(display_filename) #处理文件名中的特殊字符
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            attachment['content-type'] = 'application/octet-stream' #设置附件类型为二进制流
            attachment['content-disposition'] = f'attachment; filename = "{display_filename}"'  #设置附件的文件名
            email.attach(attachment)
    smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) #使用SSL加密连接指定服务器
    smtp.login(EMAIL_USER, EMAIL_AUTH)
    smtp.sendmail(from_user, to_user.split(';'), email.as_string() )
#endregion
#发送短信
#region
import random
import requests
def send_message_by_luosimao(tel, message):
    resp = requests.post(
        url = 'http://sms-api.luosimao.com/v1/send.json',
        auth = ('api', os.environ.get('LUOSIMAO_API_KEY', '')),  #API Key从环境变量读取，请勿硬编码
        data = {
            'mobile': tel,
            'message': message
        },
        timeout = 5,
        verify = False
    )
    return resp.json()
def gen_mobile_code(length = 6):    #生成随机验证码
    return ''.join(random.choices('0123456789', k = length))
def main():
    code = gen_mobile_code()
    message = f'您的短信是{code},请勿泄露给他人【Python小课】'
    print(send_message_by_luosimao('16665258605', message))
if __name__ == '__main__':
    main()
#endregion