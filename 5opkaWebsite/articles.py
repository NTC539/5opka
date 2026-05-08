import os
from bottle import response, route, request, redirect, template, static_file
from utils.article_storage import (
    load_articles, get_article_by_id, add_article,
    validate_article_fields, save_uploaded_image
)
import bottle
from datetime import datetime


@route('/articles')
def articles_page():
    """Отображает страницу со списком статей и выбранной статьёй или редактором."""
    sort = request.query.sort or 'date'
    action = request.query.action
    article_id = request.query.get('id')
    
    all_articles = load_articles()
    
    # Сортировка
    if sort == 'title':
        sorted_articles = sorted(all_articles, key=lambda a: a['title'].lower())
    else:
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
    
    main_content = None
    form_data = {}
    form_errors = {}
    
    if action == 'new':
        main_content = {'type': 'editor', 'article': None}
    elif article_id:
        article = get_article_by_id(int(article_id))
        if article:
            main_content = {'type': 'view', 'article': article}
        else:
            main_content = {'type': 'error', 'message': 'Статья не найдена'}
    else:
        if sorted_articles:
            main_content = {'type': 'view', 'article': sorted_articles[0]}
        else:
            main_content = {'type': 'info', 'message': 'Нет статей. Создайте первую!'}
   


    return template('articles',
                    year=datetime.now().year,
                    articles_list=sorted_articles,
                    current_sort=sort,
                    main=main_content,
                    form_data=form_data,
                    form_errors=form_errors)

@route('/articles/save', method='POST')
def save_article():
    author = request.forms.get('author', '').strip()
    title = request.forms.get('title', '').strip()
    content = request.forms.get('content', '')
    phone = request.forms.get('phone', '').strip()         
    
    uploaded_image = request.files.get('image')
    if uploaded_image:
        url = save_uploaded_image(uploaded_image)
        if url:
            content += f'\n\n<div><img src="{url}" alt="image" style="max-width:100%"></div>\n'
    
    errors = validate_article_fields(author, title, content, phone)   
    if errors:
        all_articles = load_articles()
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
        return template('articles',
                        year=datetime.now().year,
                        articles_list=sorted_articles,
                        current_sort='date',
                        main={'type': 'editor', 'article': None},
                        form_data={'author': author, 'title': title, 'content': content, 'phone': phone},
                        form_errors=errors)
    try:
        new_article = add_article(author, title, content, phone)   
    except ValueError as e:
        all_articles = load_articles()
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
        return template('articles',
                        year=datetime.now().year,
                        articles_list=sorted_articles,
                        current_sort='date',
                        main={'type': 'editor', 'article': None},
                        form_data={'author': author, 'title': title, 'content': content, 'phone': phone},
                        form_errors=errors)
    
    response.status = 303
    response.headers['Location'] = f'/articles?id={new_article["id"]}'
    return ''


# Маршрут для раздачи загруженных картинок
@route('/uploads/<filename:path>')
def serve_upload(filename):
    return static_file(filename, root='./uploads')