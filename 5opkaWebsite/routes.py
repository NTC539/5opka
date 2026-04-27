# -*- coding: utf-8 -*-
"""
Routes and views for the bottle application.
"""

from turtle import title
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

@route('/articles')
@view('articles')
def news():
    """Renders the articles page."""
    return dict(
        title='Статьи',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/shop')
@view('shop')
def news():
    """Renders the shop page."""
    return dict(
        title='Магазин',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/feedback')
@view('feedback')
def news():
    """Renders the feedback page."""
    return dict(
        title='Отзывы',
        message='Your application description page.',
        year=datetime.now().year
    )