import os
import json
from datetime import datetime
import uuid
import re

DATA_DIR = './data'
ARTICLES_FILE = os.path.join(DATA_DIR, 'articles.json')
UPLOAD_DIR = './uploads'

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)



def load_articles():
    if not os.path.exists(ARTICLES_FILE):
        return []
    with open(ARTICLES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_articles(articles):
    with open(ARTICLES_FILE, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def get_article_by_id(article_id):
    articles = load_articles()
    for a in articles:
        if a['id'] == article_id:
            return a
    return None

def validate_article_fields(author, title, content, phone):
    errors = {}
    
    # Автор
    if not author or not author.strip():
        errors['author'] = 'Автор не может быть пустым.'
    elif len(author) > 50:
        errors['author'] = 'Автор не должен превышать 50 символов.'
    elif re.search(r'[<>\"\'&]', author):
        errors['author'] = 'Автор не должен содержать HTML-теги или спецсимволы (< > " \' &).'
    
    # Заголовок
    if not title or not title.strip():
        errors['title'] = 'Заголовок не может быть пустым.'
    elif len(title) < 3:
        errors['title'] = 'Заголовок должен содержать минимум 3 символа.'
    elif len(title) > 100:
        errors['title'] = 'Заголовок не должен превышать 100 символов.'
    
    # Текст статьи
    if not content or not content.strip():
        errors['content'] = 'Текст статьи не может быть пустым.'
    elif len(content.strip()) < 10:
        errors['content'] = 'Текст статьи должен содержать минимум 10 символов.'
    
    # Телефон
    if not phone or not phone.strip():
        errors['phone'] = 'Телефон обязателен для заполнения.'
    else:
        phone_clean = phone.strip()
        # Проверка формата: либо +7XXXXXXXXXX, либо 8XXXXXXXXXX
        pattern_full = r'^(\+7|8)\d{10}$'
        if not re.match(pattern_full, phone_clean):
            errors['phone'] = 'Телефон должен быть в формате +7XXXXXXXXXX или 8XXXXXXXXXX (10 цифр после кода).'
        else:
            digits = phone_clean[-10:]
            if len(set(digits)) == 1:
                errors['phone'] = 'Некорректный номер телефона (все цифры одинаковые).'
    
    return errors

def add_article(author, title, content, phone):
    articles = load_articles()
    new_id = max([a['id'] for a in articles], default=0) + 1
    article = {
        "id": new_id,
        "author": author.strip(),
        "title": title.strip(),
        "content": content,
        "phone": phone.strip(),          # сохраняем номер
        "created_at": datetime.now().isoformat()
    }
    articles.append(article)
    save_articles(articles)
    return article

def save_uploaded_image(upload):
    """Сохраняет загруженное изображение и возвращает URL. Если файла нет – возвращает None."""
    if not upload or not upload.file:
        return None
    filename = upload.filename
    ext = os.path.splitext(filename)[-1].lower()
    if ext not in ('.png', '.jpg', '.jpeg', '.gif'):
        return None
    safe_name = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, safe_name)
    with open(filepath, 'wb') as f:
        f.write(upload.file.read())
    return f"/uploads/{safe_name}"