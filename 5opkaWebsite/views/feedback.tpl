% rebase('layout.tpl', title=title, year=year)
<%
    from bottle import response
    response.set_header('Content-Type', 'text/html; charset=utf-8')
%>

<link rel="stylesheet" type="text/css" href="/static/content/feedback.css" />

<div class="feedback-container">
    <h1 class="heading-text" style="padding: 0 400px; margin: 30px 0 20px 0;">Отзывы</h1>

    <!-- Форма добавления отзыва -->
    <div style="padding: 0 400px; margin-bottom: 30px;">
        <div style="background-color: var(--main-color); padding: 25px; border-radius: 8px;">
            <h2 class="regular-text" style="font-weight: bold; margin-bottom: 20px;">Оставить отзыв</h2>

            <form method="post" action="/feedback">
                <div style="margin-bottom: 15px;">
                    <label for="author" class="regular-text" style="font-size: 14pt; display: block; margin-bottom: 8px;">Ваше имя или ник *</label>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 16pt;">👤</span>
                        <input type="text" id="author" name="author"
                               value="{{form_data.get('author', '')}}"
                               placeholder="Введите имя"
                               style="flex: 1; max-width: 450px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: var(--main-font); {{'border-color: #b94a48; background-color: #fff5f5;' if errors.get('author') else ''}}">
                    </div>
                    % if errors.get('author'):
                        <div style="color: #b94a48; font-size: 12pt; margin-top: 5px; margin-left: 30px;">{{errors['author']}}</div>
                    % end
                </div>

                <div style="margin-bottom: 15px;">
                    <label for="email" class="regular-text" style="font-size: 14pt; display: block; margin-bottom: 8px;">Email *</label>
                    <div style="display: flex; align-items: center; gap: 10px;">
                        <span style="font-size: 16pt;">✉️</span>
                        <input type="email" id="email" name="email"
                               value="{{form_data.get('email', '')}}"
                               placeholder="example@mail.ru"
                               style="flex: 1; max-width: 450px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: var(--main-font); {{'border-color: #b94a48; background-color: #fff5f5;' if errors.get('email') else ''}}">
                    </div>
                    % if errors.get('email'):
                        <div style="color: #b94a48; font-size: 12pt; margin-top: 5px; margin-left: 30px;">{{errors['email']}}</div>
                    % end
                </div>

                <div style="margin-bottom: 15px;">
                    <label for="text" class="regular-text" style="font-size: 14pt; display: block; margin-bottom: 8px;">Текст отзыва *</label>
                    <div style="display: flex; align-items: flex-start; gap: 10px;">
                        <span style="font-size: 16pt;">💬</span>
                        <textarea id="text" name="text" rows="4"
                                  style="flex: 1; max-width: 600px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; font-family: var(--main-font); resize: vertical; {{'border-color: #b94a48; background-color: #fff5f5;' if errors.get('text') else ''}}">{{form_data.get('text', '')}}</textarea>
                    </div>
                    % if errors.get('text'):
                        <div style="color: #b94a48; font-size: 12pt; margin-top: 5px; margin-left: 30px;">{{errors['text']}}</div>
                    % end
                </div>

                <button type="submit" style="background-color: var(--main-color); border: none; padding: 10px 25px; font-family: var(--main-font); font-size: 14pt; font-weight: bold; cursor: pointer; border-radius: 5px; transition: opacity 0.3s; margin-top: 10px;"
                        onmouseover="this.style.opacity='0.7'" onmouseout="this.style.opacity='1'">Отправить отзыв</button>
            </form>
        </div>
    </div>

    <!-- Список отзывов -->
    <div class="news-container" style="padding-bottom: 50px;">
        % if not feedbacks:
            <div style="text-align: center; padding: 50px; background-color: rgba(0,0,0,0.02); border-radius: 10px;">
                <p class="regular-text" style="color: rgba(0,0,0,0.5);">Пока нет отзывов. Будьте первым!</p>
            </div>
        % else:
            % for fb in feedbacks:
                <div class="news-block">
                    <div>
                        <div style="background-color: rgba(0, 0, 0, 0.02); border-radius: 5px; padding: 20px;">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 2px solid var(--main-color); padding-bottom: 10px;">
                                <div>
                                    <strong style="font-size: 16pt; font-family: var(--main-font);">{{fb['author']}}</strong>
                                    % if fb.get('email'):
                                        <div style="font-size: 10pt; color: rgba(0,0,0,0.5); font-family: var(--main-font); margin-top: 4px;">
                                            ✉️ {{fb['email']}}
                                        </div>
                                    % end
                                </div>
                                <span style="font-size: 11pt; color: rgba(0,0,0,0.55); font-family: var(--main-font);">
                                    📅 {{fb['date']}}
                                </span>
                            </div>
                            <p style="font-family: var(--main-font); font-size: 14pt; line-height: 1.5; margin: 0; color: rgba(0,0,0,0.8);">
                                💬 {{fb['text']}}
                            </p>
                        </div>
                    </div>
                </div>
            % end
        % end
    </div>
</div>

<script>
    // Плавное появление карточек
    const cards = document.querySelectorAll('.news-block');
    cards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.4s ease ${index * 0.1}s, transform 0.4s ease ${index * 0.1}s`;

        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, 100);
    });
</script>