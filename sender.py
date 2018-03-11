import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(name,frm,text):
    my_email='no-reply@nikitonsky.tk'
    server = smtplib.SMTP_SSL('smtp.yandex.ru')
    server.login(my_email, 'qwerty123')
    msg = MIMEText('Имя:{name}\n\n{text}'.format(name=name,text=text), 'plain', 'utf-8')
    msg['Subject'] = Header('Новый отзыв на сайте', 'utf-8')
    msg['From'] = frm
    msg['To'] = my_email
    server.sendmail(my_email, my_email, msg.as_string())
    server.quit()
