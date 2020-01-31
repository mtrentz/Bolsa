import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(to_mail, positive, negative):
    """
    Sends an email of investment rentability.
    ALl other info is foudn and created in in email_generator.py
    Args:
        to_mail: email of reciever
        positive: stock symb that had best performance
        negative: stock symb with worst performance
    """
    # Email Info
    # todo esconder info
    email_address = 'tz.bolsa@gmail.com'
    email_password = 'v4it3fud3'

    msg = MIMEMultipart()
    msg['Subject'] = 'Suas Ações!'
    msg['From'] = email_address
    msg['to'] = to_mail

    # todo add texto melhor
    plain_msg = MIMEText('Habilite html para visualizar e-mail', 'plain', 'utf-8')
    msg.attach(plain_msg)

    # html of the newsletter
    html = open('newsletter.html', encoding='utf-8')
    msg.attach(MIMEText(html.read(), 'html', 'utf-8'))

    # Attachments to show inline, numbered in imglist order. Shows as 'cid:i' on html file.
    imglist = ['rentability.png', 'portfolio.png', 'bars.png', f'{positive}.png', f'{negative}.png']
    i = 0
    for img in imglist:
        with open(f'Figures\\{img}', 'rb') as f:
            mime = MIMEBase('image', 'png', filename=f'{img}')
            mime.add_header('Content-Disposition', 'attachment', filename=f'{img}')
            mime.add_header('X-Attachment-Id', f'{i}')
            mime.add_header('Content-ID', f'<{i}>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
            i += 1

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)


