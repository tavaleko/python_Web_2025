# mail_test.py
# pip install python-dotenv
from send_mail import send_mail
from dotenv import load_dotenv

send_mail('tyttsy@mail.ru', 'Вам письмо', 'Текст письма')