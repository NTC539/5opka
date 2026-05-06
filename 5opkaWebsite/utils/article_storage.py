
import os
import json
from datetime import datetime

DATA_DIR = './data'
ARTICLES_FILE = os.path.join(DATA_DIR, 'articles.json')
UPLOAD_DIR = './uploads'

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)

def load_articles():
    """Загружает все статьи из JSON."""
    if not os.path.exists(ARTICLES_FILE):
        sample = [{
            "id": 1,
            "author": "5opka Team",
            "title": "Как стать популярным стримером",
            "content": "<p>Уникальный контент, регулярные стримы, общение с аудиторией — главные секреты.</p><img src='/uploads/example.jpg' alt='example' style='max-width:100%'>",
            "created_at": datetime.now().isoformat()
        }]
        save_articles(sample)
        return sample
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

def add_article(author, title, content):
    articles = load_articles()
    new_id = max([a['id'] for a in articles], default=0) + 1
    article = {
        "id": new_id,
        "author": author.strip(),
        "title": title.strip(),
        "content": content,
        "created_at": datetime.now().isoformat()
    }
    articles.append(article)
    save_articles(articles)
    return article



def validate_article_fields(author, title, content):
    errors = {}
    if not author or not author.strip():
        errors['author'] = 'Укажите автора.'
    if not title or not title.strip():
        errors['title'] = 'Введите заголовок.'
    if not content or not content.strip():
        errors['content'] = 'Текст статьи не может быть пустым.'
    return errors

def save_uploaded_image(file_data, filename):
    """Сохраняет загруженный файл и возвращает URL."""
    import uuid
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ('.png', '.jpg', '.jpeg', '.gif'):
        return None
    safe_name = f"{uuid.uuid4().hex}{ext}"
    filepath = os.path.join(UPLOAD_DIR, safe_name)
    with open(filepath, 'wb') as f:
        f.write(file_data.file.read())
    return f"/uploads/{safe_name}"