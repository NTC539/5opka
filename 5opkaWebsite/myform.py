import re
import pdb
from bottle import post, request, template
from datetime import datetime


user_questions = {}

def is_valid_email(email):
    """
    Функция для, проверка корректности email почты
    """
    # Регулярное выражение для, проверка
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    # Проверка выражение
    if not re.fullmatch(pattern, email):
        return False

    # Проверка на реальные домены
    valid_domains = [
        'gmail.com', 'mail.ru', 'yandex.ru', 'ya.ru',
        'outlook.com',  'rambler.ru'
    ]

    local_part, domain = email.split('@')

    # Проверка длины
    if len(local_part) > 40:
        return False

    # Переводим в нижний регистр
    domain_lower = domain.lower()

    for valid_domain in valid_domains:
        if domain_lower == valid_domain:
            return True

    return False


@post('/home', method='post')
def my_form():
    # Получение данных от пользователя.
    mail = request.forms.get('ADRESS').strip()
    quest = request.forms.get('QUEST').strip()
    name = request.forms.get('USERNAME').strip()

    # Проверка, что пользователь ввел данные
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

    # Проверка коректности почты
    if not is_valid_email(mail):
        return template('error',
            title="Ошибка!",
            message="email в неправильном формате"
        )

    user_questions[mail] = [name, quest]
    pdb.set_trace()

    return "Thanks! %s The answer will be sent to the mail %s Access Date: %s" % (name, mail, datetime.now().strftime("%Y-%m-%d"))
