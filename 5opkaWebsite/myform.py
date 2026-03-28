import re
import pdb
import json
import os
from datetime import datetime
from dotenv import load_dotenv

from bottle import post, request, template


load_dotenv()

DATA_FILE = os.environ.get('DATA_FILE')

def load_questions() -> dict:
    """Загрузка данных из JSON-файла"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}

    return {}

def save_questions(data: dict[str, str]):
    """

    """
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def is_valid_question(question: str) -> tuple[bool, str]:
    """
    - длина более 3 символов
    - не состоит только из цифр
    - не состоит только из спецсимволов (&&&, ???, !!! и т.п.)
    - должен содержать хотя бы одну букву (русскую или английскую)
    - не пустой после очистки
    """
    question = question.strip()

    # Проверка длины
    if len(question) <= 3:
        return False, "Вопрос должен содержать более 3 символов"

    # Проверка: не состоит только из цифр
    if question.isdigit():
        return False, "Вопрос не может состоять только из цифр"

    has_letter = bool(re.search(r'[a-zA-Zа-яА-ЯёЁ]', question))

    if not has_letter:
        return False, "Вопрос должен содержать хотя бы одну букву"

    return True, ""

def is_valid_email(email: str) -> bool:
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

    # Проверка корректности почты
    if not is_valid_email(mail):
        return template('error',
            title="Ошибка!",
            message="email в неправильном формате"
        )

    # ПРОВЕРКА КОРРЕКТНОСТИ ВОПРОСА (ДОБАВИТЬ ЭТОТ БЛОК)
    is_valid, error_msg = is_valid_question(quest)
    if not is_valid:
        return template('error',
            title="Ошибка!",
            message=error_msg
        )

    # Загружаем существующие данные
    user_questions = load_questions()

    # Добавляем новые данные
    if mail in user_questions:
        # У пользователя уже есть вопросы
        existing_questions = user_questions[mail]
        # Проверяем на дубликат вопроса
        if quest not in existing_questions:
            existing_questions.append(quest)
            user_questions[mail] = existing_questions
    else:
        # Новый пользователь — создаем запись
        user_questions[mail] = [quest]

    save_questions(user_questions)

    pdb.set_trace()

    return "Thanks! %s The answer will be sent to the mail %s Access Date: %s" % (name, mail, datetime.now().strftime("%Y-%m-%d"))