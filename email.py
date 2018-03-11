import smtplib

class sender:
    def __init__(self):
        email='baza86163919@gmail.com'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        #print(server.help())
        server.starttls()
        server.login(email, '86163919')

    def send(self, name,dest_email,email_text):
        subject = 'Новый отзыв'
        message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(dest_email,
                                                       email,
                                                       subject,
                                                       email_text)
        server.sendmail(email, email, message)
    def __del__(self):
        server.quit()

#a = sender()
#a.send('aa', 'aa@aa.a', 'test')
print(help('smtplib'))
