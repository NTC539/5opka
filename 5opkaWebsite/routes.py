# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from bottle import route, view, template, request, redirect, response
import json
import os
from datetime import datetime

# Данные для таймлайна
timeline_data = {
    '1996': {'age': 0, 'title': 'Детство и юность'},
    '2011': {'age': 15, 'title': 'Зарождение легенды'},
    '2016': {'age': 20, 'title': 'Расцвет стриминга'},
    '2022': {'age': 26, 'title': 'Мемная популярность'},
    '2024': {'age': 28, 'title': 'Альбом "1000 жизней"'},
    '2025': {'age': 29, 'title': 'Триумф и эпатаж'}
}

# Получаем последний год для отображения по умолчанию
last_year = list(timeline_data.keys())[-1]  # '2025'

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        title='Главная',
        year=datetime.now().year
    )

@route('/career')
@view('career')
def career():
    """Страница карьеры с последним годом по умолчанию"""
    # Загружаем шаблон для последнего года
    year_template = template("career/" + last_year)
    return dict(
                   title='Карьера',
                   year=datetime.now().year,
                   timeline_data=timeline_data,
                   selected_year=last_year,
                   year_content=year_template)

@route('/career/<year>')
@view('/career/<year>')
def career_year(year):
    """Страница карьеры с выбранным годом"""
    if year in timeline_data:
        # Загружаем шаблон для выбранного года
        year_template = template("career/" + year)
        return template('career',
                       title='Карьера',
                       year=datetime.now().year,
                       timeline_data=timeline_data,
                       selected_year=year,
                       year_content=year_template)
    else:
        # Если год не найден, показываем последний
        year_template = template("career/" + last_year)
        return template('career',
                       title='Карьера',
                       year=datetime.now().year,
                       timeline_data=timeline_data,
                       selected_year=last_year,
                       year_content=year_template)

@route('/news')
@view('news')
def news():
    """Renders the news page."""
    return dict(
        title='Новости',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/galery')
@view('galery')
def galery():
    """Renders the galery page."""
    return dict(
        title='Галерея',
        message='Your application description page.',
        year=datetime.now().year
    )

track_list = ['empty', 'zmiShare', '42', 'venomBoy', '1000zhizney', 'slavaBossu', 'golovolomka']
default_track = track_list[0]

@route('/music')
@view('music')
def music():
    """Страница музыки с треком по умолчанию"""
    track_content = template('music/' + default_track)
    return dict(
        title='Музыка',
        year=datetime.now().year,
        music_content=track_content,
        selected_track=default_track,
        track_list=track_list
    )

@route('/music/<track_name>')
@view('music')
def music_track(track_name):
    """Страница музыки с выбранным треком"""
    if track_name in track_list:
        track_content = template('music/' + track_name)
    else:
        track_content = template('music/' + default_track)
        track_name = default_track
    return dict(
        title='Музыка',
        year=datetime.now().year,
        music_content=track_content,
        selected_track=track_name,
        track_list=track_list
    )


@route('/shop')
@view('shop')
def shop():
    """Renders the shop page."""
    return dict(
        title='Магазин',
        message='Your application description page.',
        year=datetime.now().year
    )


FEEDBACK_FILE = os.path.join(os.path.dirname(__file__), 'data', 'feedback.json')


def load_feedback():
    """Загружает отзывы из JSON файла"""
    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)

    if not os.path.exists(FEEDBACK_FILE):
        return []

    try:
        with open(FEEDBACK_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception) as e:
        print(f"Ошибка загрузки отзывов: {e}")
        return []

def is_valid_email(email: str) -> bool:
    import re
    """Проверка корректности email почты"""
    if not email or not isinstance(email, str):
        return False

    if email != email.strip() or ' ' in email:
        return False

    email = email.strip()

    if email.startswith('.'):
        return False

    pattern = r'^[a-zA-Z0-9_.+%-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

    if not re.fullmatch(pattern, email):
        return False

    try:
        local_part, domain = email.split('@')
    except ValueError:
        return False

    if local_part.startswith('.') or local_part.endswith('.'):
        return False

    if '..' in local_part or '..' in domain:
        return False

    if len(local_part) > 40:
        return False

    valid_domains = [
        'gmail.com', 'mail.ru', 'yandex.ru', 'ya.ru',
        'outlook.com', 'rambler.ru'
    ]

    return domain.lower() in valid_domains

def save_feedback(feedback_list):
    """Сохраняет отзывы в JSON файл"""
    try:
        os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)
        with open(FEEDBACK_FILE, 'w', encoding='utf-8') as f:
            json.dump(feedback_list, f, ensure_ascii=False, indent=2)
        print(f"Сохранено {len(feedback_list)} отзывов")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")


@route('/feedback')
@view('feedback')
def feedback():
    """Renders the feedback page."""
    feedback_list = load_feedback()
    feedback_list.sort(key=lambda x: x.get('date', ''), reverse=True)
    return dict(
        title='Отзывы',
        year=datetime.now().year,
        feedbacks=feedback_list,
        form_data={},
        errors={}
    )


@route('/feedback', method='POST')
def feedback_post():
    """POST: Обрабатывает отправку нового отзыва"""

    author = request.forms.get('author', '')
    email = request.forms.get('email', '')
    text = request.forms.get('text', '')

    def fix_encoding(s):
        if isinstance(s, str):
            try:
                return s.encode('raw_unicode_escape').decode('utf-8')
            except:
                try:
                    return s.encode('latin-1').decode('utf-8')
                except:
                    return s
        return s

    author = fix_encoding(author).strip()
    email = fix_encoding(email).strip()
    text = fix_encoding(text).strip()

    errors = {}

    if not author:
        errors['author'] = 'Введите имя или ник'
    elif len(author) < 2:
        errors['author'] = 'Имя должно содержать хотя бы 2 символа'

    if not email:
        errors['email'] = 'Введите email'
    elif not is_valid_email(email):
        errors['email'] = 'Введите корректный email'

    if not text:
        errors['text'] = 'Введите текст отзыва'
    elif len(text) < 5:
        errors['text'] = 'Текст отзыва должен содержать хотя бы 5 символов'

    feedback_list = load_feedback()

    if errors:
        feedback_list.sort(key=lambda x: x.get('date', ''), reverse=True)
        return template('feedback',
                        title='Отзывы',
                        year=datetime.now().year,
                        feedbacks=feedback_list,
                        form_data={'author': author, 'email': email, 'text': text},
                        errors=errors)

    new_feedback = {
        'author': author,
        'email': email,
        'text': text,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M')
    }
    feedback_list.append(new_feedback)
    save_feedback(feedback_list)

    response.status = 303
    response.headers['Location'] = '/feedback'
