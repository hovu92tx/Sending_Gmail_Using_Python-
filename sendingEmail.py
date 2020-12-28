import smtplib


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your email', 'password')
    sendTo = input('To: ')
    subject = input('Subject: ')
    body = input('Message: ')
    msg = f'subject:{subject} \n\n\n {body}'
    server.sendmail(
        # From
        'your email',
        # To
        sendTo,
        msg
    )
    print('Email is sent!!')


if __name__ == '__main__':
    send_email()
