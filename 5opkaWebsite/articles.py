import os
from bottle import route, request, redirect, template, static_file
from utils.article_storage import (
    load_articles, get_article_by_id, add_article,
    validate_article_fields, save_uploaded_image
)
from datetime import datetime

@route('/articles')
def articles_page():
    """Отображает страницу со списком статей (левая панель) и выбранной статьёй или редактором."""
    
    # Получаем параметры из URL
    sort = request.query.sort or 'date'      # 'date' или 'title'
    action = request.query.action             # 'edit' для редактора
    article_id = request.query.get('id')      # ID статьи для просмотра
    
    # Загружаем все статьи
    all_articles = load_articles()
    
    # Сортировка
    if sort == 'title':
        sorted_articles = sorted(all_articles, key=lambda a: a['title'].lower())
    else:  # date
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
    
    # Определяем, что показывать в основной области
    main_content = None
    form_data = {}
    form_errors = {}
    
    if action == 'new':
        # Показываем редактор для новой статьи
        main_content = {
            'type': 'editor',
            'article': None
        }
    elif article_id:
        article = get_article_by_id(int(article_id))
        if article:
            main_content = {
                'type': 'view',
                'article': article
            }
        else:
            main_content = {'type': 'error', 'message': 'Статья не найдена'}
    else:
        # По умолчанию – первая статья из отсортированного списка
        if sorted_articles:
            main_content = {
                'type': 'view',
                'article': sorted_articles[0]
            }
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
    """Обработка сохранения новой статьи."""
    author = request.forms.get('author', '')
    title = request.forms.get('title', '')
    content = request.forms.get('content', '')
    
    # Валидация
    errors = validate_article_fields(author, title, content)
    if errors:
        # При ошибках возвращаемся в редактор с ошибками и уже введёнными данными
        all_articles = load_articles()
        sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
        return template('articles',
                        year=datetime.now().year,
                        articles_list=sorted_articles,
                        current_sort='date',
                        main={'type': 'editor', 'article': None},
                        form_data={'author': author, 'title': title, 'content': content},
                        form_errors=errors)
    
    # Сохраняем статью
    new_article = add_article(author, title, content)
    # Перенаправляем на страницу новой статьи
    redirect(f'/articles?id={new_article["id"]}')

@route('/articles/upload_image', method='POST')
def upload_image():
    """Загружает изображение и возвращается обратно в редактор (с сохранением текста)."""
    # Получаем текущие данные формы (передаём через скрытые поля)
    author = request.forms.get('author', '')
    title = request.forms.get('title', '')
    content = request.forms.get('content', '')
    upload = request.files.get('image')
    
    image_url = None
    if upload:
        image_url = save_uploaded_image(upload, upload.filename)
        if image_url:
            # Добавляем тег img в конец содержимого (или можно вставить по курсору, но без JS это сложно)
            content += f'\n<img src="{image_url}" alt="image" style="max-width:100%">\n'
    
    # Возвращаемся в редактор с обновлённым содержимым
    all_articles = load_articles()
    sorted_articles = sorted(all_articles, key=lambda a: a['created_at'], reverse=True)
    return template('articles',
                    year=datetime.now().year,
                    articles_list=sorted_articles,
                    current_sort='date',
                    main={'type': 'editor', 'article': None},
                    form_data={'author': author, 'title': title, 'content': content},
                    form_errors={})

# Раздача загруженных картинок
@route('/uploads/<filename:path>')
def serve_upload(filename):
    return static_file(filename, root='./uploads')