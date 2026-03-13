import re

from bottle import post, request, template
from datetime import datetime


def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.fullmatch(pattern, email):
        return False

    # Проверка на реальные домены
    valid_domains = [
        'gmail.com', 'mail.ru', 'yandex.ru', 'ya.ru',
        'outlook.com',  'rambler.ru'
    ]

    domain = email.split('@')[1].lower()

    for valid_domain in valid_domains:
        if domain == valid_domain:
            return True

    return False


@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS').strip()
    quest = request.forms.get('QUEST').strip()
    name = request.forms.get('USERNAME').strip()

    if not mail:
        return template('error',
            title="Ошибка!",
            message="Пожалуйста, заполните форму email."
        )
    elif not quest:
        return template('error',
            title="Ошибка!",
            message="Пожалуйста, заполните заполните форму вопроса."
        )
    elif not name:
        return template('error',
            title="Ошибка!",
            message="Пожалуйста, заполните заполните форму имени."
        )

    if not is_valid_email(mail):
        return template('error',
            title="Ошибка!",
            message="email в неправильном формате"
        )

    return "Thanks! %s The answer will be sent to the mail %s Access Date: %s" % (name, mail, datetime.now().strftime("%Y-%m-%d"))
