from smtplib import SMTP
from email.mime.text import MIMEText
from email.header import Header

mail_server = "smtp.qq.com"
port = '25' # default for SMTP

def get_mail_server(sender):
    key = sender[sender.index('@')+1:]
    return "smtp."+key

sender = '980068028@qq.com'
sender_pass = 'tkpckcavhrrpbfje'
receiver = 'u6102560@anu.edu.au'
mail_server = get_mail_server(sender=sender)

mail_msg = """我是邪恶王逸凡 我要取代你!"""
msg = MIMEText(_text=mail_msg, _subtype='plain', _charset='utf-8')
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = Header('from 邪恶王逸凡','utf-8')

try:
    server = SMTP(host=mail_server, port=port)
    # server.set_debuglevel(1)
    server.login(sender, sender_pass)
    server.sendmail(from_addr=sender, to_addrs=[receiver], msg=msg.as_string())
    server.quit()
    print("Success!")
except:
    server.quit()
    print('Fail!')
