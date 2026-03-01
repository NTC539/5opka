# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from bottle import route, view, template
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
        year=datetime.now().year
    )

@route('/career')
@view('career')
def career():
    """Страница карьеры с последним годом по умолчанию"""
    # Загружаем шаблон для последнего года
    year_template = template("career/" + last_year)
    return dict(
                   title='Career',
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
                       title='Career',
                       year=datetime.now().year,
                       timeline_data=timeline_data,
                       selected_year=year,
                       year_content=year_template)
    else:
        # Если год не найден, показываем последний
        year_template = template("career/" + last_year)
        return template('career',
                       title='Career',
                       year=datetime.now().year,
                       timeline_data=timeline_data,
                       selected_year=last_year,
                       year_content=year_template)

@route('/news')
@view('news')
def news():
    """Renders the news page."""
    return dict(
        title='News',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/music')
@view('music')
def music():
    """Renders the music page."""
    return dict(
        title='Music',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/galery')
@view('galery')
def galery():
    """Renders the galery page."""
    return dict(
        title='Galery',
        message='Your application description page.',
        year=datetime.now().year
    )