# enviando emails smtp com python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path
from string import Template

from dotenv import load_dotenv

load_dotenv()

# path to html
HTML_PATH = Path(__file__).parent / "aula176.html"

# remetente e destinatario
sender = os.getenv("FROM_EMAIL", "")
receiver = sender

# configuracoes SMTP
smtp_server = os.getenv("KH_SERVER", "")
smtp_port = int(os.getenv("KH_PT", ""))
smtp_username = sender
smtp_password = os.getenv("EMAIL_PWD", "")


# msg
with HTML_PATH.open(mode='r') as file:
    text = file.read()
    template = Template(text)
    mail_text = template.safe_substitute(nome="Fulano")

# transforma msg to MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart["from"] = sender
mime_multipart["to"] = receiver
mime_multipart["subject"] = "O assunto do email"

mail_body = MIMEText(mail_text, "html", "utf-8")
mime_multipart.attach(mail_body)

# send mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print("E-mail enviado com sucesso")
