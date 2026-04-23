import re
import pdb
import json
import os
from datetime import datetime
from dotenv import load_dotenv

from bottle import post, request, template

load_dotenv()

DATA_FILE = os.environ.get('DATA_FILE', 'user_questions.json')


def load_questions() -> dict:
    """Загрузка данных из JSON-файла"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
        except Exception as error:
            return {}
    return {}


def save_questions(data: dict):
    """Сохранение данных в JSON-файл"""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def is_valid_question(question: str) -> tuple[bool, str]:
    """
    Проверка корректности вопроса:
    - длина более 3 символов
    - не состоит только из цифр
    - не состоит только из спецсимволов (&, ?, ! и т.п.)
    - должен содержать хотя бы одну букву
    """
    question = question.strip()

    if len(question) <= 3:
        return False, "Вопрос должен содержать более 3 символов"

    if question.isdigit():
        return False, "Вопрос не может состоять только из цифр"

    # Проверка: есть хотя бы одна буква (русская или английская)
    has_letter = bool(re.search(r'[a-zA-Zа-яА-ЯёЁ]', question))
    if not has_letter:
        return False, "Вопрос должен содержать хотя бы одну букву"

    return True, ""


def is_valid_email(email: str) -> bool:
    """Проверка корректности email почты"""
    if not email or not isinstance(email, str):
        return False

    # Проверка на пробелы в начале, в конце и внутри
    if email != email.strip() or ' ' in email:
        return False

    email = email.strip()

    # Проверка: не начинается с точки
    if email.startswith('.'):
        return False

    # Регулярное выражение (добавлен % в локальную часть)
    pattern = r'^[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    if not re.fullmatch(pattern, email):
        return False

    # Дополнительные проверки локальной части
    try:
        local_part, domain = email.split('@')
    except ValueError:
        return False

    # Точка не в начале и не в конце локальной части
    if local_part.startswith('.') or local_part.endswith('.'):
        return False

    # Нет двух точек подряд
    if '..' in local_part or '..' in domain:
        return False

    # Длина локальной части не более 40 символов
    if len(local_part) > 40:
        return False

    # Проверка домена по списку
    valid_domains = [
        'gmail.com', 'mail.ru', 'yandex.ru', 'ya.ru',
        'outlook.com', 'rambler.ru'
    ]

    return domain.lower() in valid_domains


def is_valid_name(name: str) -> tuple[bool, str]:
    """Проверка корректности имени"""
    name = name.strip()

    if not name:
        return False, "Имя не может быть пустым"

    if len(name) < 2:
        return False, "Имя должно содержать не менее 2 символов"

    # Имя должно содержать только буквы, пробелы, дефисы
    if not re.match(r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$', name):
        return False, "Имя может содержать только буквы, пробелы и дефисы"

    return True, ""


@post('/home', method='post')
def my_form():
    # Получение данных от пользователя
    mail = request.forms.get('ADRESS', '').strip()
    quest = request.forms.get('QUEST', '').strip()
    name = request.forms.get('USERNAME', '').strip()

    # Проверка, что пользователь ввел данные
    if not mail:
        return template('error',
                        title="Ошибка!",
                        message="Пожалуйста, заполните поле email."
                        )
    elif not quest:
        return template('error',
                        title="Ошибка!",
                        message="Пожалуйста, заполните поле вопроса."
                        )
    elif not name:
        return template('error',
                        title="Ошибка!",
                        message="Пожалуйста, заполните поле имени."
                        )

    # Проверка корректности имени
    is_valid_name_flag, name_error = is_valid_name(name)
    if not is_valid_name_flag:
        return template('error',
                        title="Ошибка!",
                        message=name_error
                        )

    # Проверка корректности почты
    if not is_valid_email(mail):
        return template('error',
                        title="Ошибка!",
                        message="Email в неправильном формате. Допустимые домены: gmail.com, mail.ru, yandex.ru, ya.ru, outlook.com, rambler.ru"
                        )

    # Проверка корректности вопроса
    is_valid_quest_flag, quest_error = is_valid_question(quest)
    if not is_valid_quest_flag:
        return template('error',
                        title="Ошибка!",
                        message=quest_error
                        )

    # Загружаем существующие данные
    user_questions = load_questions()

    if mail in user_questions:
        # Пользователь уже существует
        existing_data = user_questions[mail]

        # Обновляем имя (если оно изменилось)
        existing_data['name'] = name

        # Проверяем на дубликат вопроса
        if quest not in existing_data['questions']:
            existing_data['questions'].append(quest)

        user_questions[mail] = existing_data
    else:
        # Новый пользователь — создаем запись
        user_questions[mail] = {
            "name": name,
            "questions": [quest]
        }

    save_questions(user_questions)

    pdb.set_trace()

    return "Thanks, %s! Your question '%s' has been saved. Answer will be sent to %s. Date: %s" % (
        name, quest, mail, datetime.now().strftime("%Y-%m-%d")
    )