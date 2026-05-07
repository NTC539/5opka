import os
from bottle import route, request, redirect, template, static_file
from utils.article_storage import (
    load_articles, get_article_by_id, add_article,
    validate_article_fields, save_uploaded_image
)
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
    
    # Определяем, что показывать в основной области
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
    """Обработка сохранения новой статьи (с возможной загрузкой изображения)."""
    author = request.forms.get('author', '').strip()
    title = request.forms.get('title', '').strip()
    content = request.forms.get('content', '')
    uploaded_image = request.files.get('image')
    
    # Если загружено изображение – сохраняем и добавляем тег в конец текста
    image_url = save_uploaded_image(uploaded_image)
    if image_url:
        content += f'\n\n<img src="{image_url}" alt="image" style="max-width:100%">\n'
    
    # Валидация
    errors = validate_article_fields(author, title, content)
    if errors:
        # Возвращаем в редактор с ошибками
        all_articles = load_articles()
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
        return template('articles',
                        year=datetime.now().year,
                        articles_list=sorted_articles,
                        current_sort='date',
                        main={'type': 'editor', 'article': None},
                        form_data={'author': author, 'title': title, 'content': content},
                        form_errors=errors)
    
    try:
        new_article = add_article(author, title, content)
    except ValueError as e:
        # Ошибка при добавлении (например, пустые поля)
        all_articles = load_articles()
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
        return template('articles',
                        year=datetime.now().year,
                        articles_list=sorted_articles,
                        current_sort='date',
                        main={'type': 'editor', 'article': None},
                        form_data={'author': author, 'title': title, 'content': content},
                        form_errors={'general': str(e)})
    
    # Успех – перенаправляем на созданную статью
    redirect(f'/articles')

# Маршрут для раздачи загруженных картинок
@route('/uploads/<filename:path>')
def serve_upload(filename):
    return static_file(filename, root='./uploads')