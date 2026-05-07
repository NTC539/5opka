% rebase('layout.tpl', title='Полезные статьи', year=year)

<link rel="stylesheet" href="/static/content/articles.css">

<div class="articles-layout">
    <aside class="sidebar">
        <div class="sidebar-header">
            <a href="/articles?action=new" class="btn-new">Написать статью</a>
            <div class="sort-buttons">
                <a href="/articles?sort=date" class="sort-btn {{'active' if current_sort=='date' else ''}}">По дате</a>
                <a href="/articles?sort=title" class="sort-btn {{'active' if current_sort=='title' else ''}}">По алфавиту</a>
            </div>
        </div>
        <div class="articles-list">
            % for article in articles_list:
            <a href="/articles?id={{article['id']}}" class="article-item">
                <h4>{{article['title']}}</h4>
                <p>{{article['author']}} • {{article['created_at'][:10]}}</p>
            </a>
            % end
            % if not articles_list:
            <p class="empty">Статей пока нет</p>
            % end
        </div>
    </aside>

    <main class="sas">
        % if main['type'] == 'view':
            <div class="article-view">
                <h1 class="heading-text">{{main['article']['title']}}</h1>
                <div class="article-meta regular-text">
                    Автор: {{main['article']['author']}} • 
                    Дата: {{main['article']['created_at'][:10]}}
                </div>
                <div class="article-content regular-text">
                    {{! main['article']['content']}}
                </div>
            </div>
        % elif main['type'] == 'editor':
            <div class="editor-form">
                <h2 class="heading-text">Новая статья</h2>
                % if form_errors:
                <div class="error-message">
                    <strong>Исправьте ошибки:</strong>
                    <ul>
                        % for err in form_errors.values():
                        <li>{{err}}</li>
                        % end
                    </ul>
                </div>
                % end
                <form method="post" action="/articles/save" enctype="multipart/form-data">
                    <div class="form-group">
                        <label class="regular-text">Автор</label>
                        <input type="text" name="author" value="{{form_data.get('author', '')}}" required>
                    </div>
                    <div class="form-group">
                        <label class="regular-text">Заголовок</label>
                        <input type="text" name="title" value="{{form_data.get('title', '')}}" required>
                    </div>
                    <div class="form-group">
                        <label class="regular-text">Текст статьи (можно использовать HTML)</label>
                        <textarea name="content" required>{{form_data.get('content', '')}}</textarea>
                    </div>
                    <div class="form-group">
                        <label class="regular-text">Изображение (будет добавлено в конец статьи)</label>
                        <input type="file" name="image" accept="image/*">
                    </div>
                    <button type="submit" class="btn-submit">Опубликовать</button>
                </form>
            </div>
        % elif main['type'] == 'error':
            <div class="error-message">{{main['message']}}</div>
        % else:
            <div class="placeholder regular-text">
                {{main.get('message', 'Выберите статью из списка или создайте новую')}}
            </div>
        % end
    </main>
</div>