% rebase('layout.tpl', title=title, year=year)
<%
    from bottle import response
    response.set_header('Content-Type', 'text/html; charset=utf-8')
%>

<link rel="stylesheet" type="text/css" href="/static/content/feedback.css" />

<div class="feedback-page">
    <!-- Hero секция -->
    <div class="feedback-hero">
        <div class="feedback-hero-content">
            <div class="hero-badge">💬 Нам важно ваше мнение</div>
            <h1 class="feedback-hero-title">Отзывы</h1>
            <p class="feedback-hero-subtitle">Что говорят о нас слушатели</p>
        </div>
    </div>

    <!-- Форма отзыва -->
    <div class="feedback-form-section">
        <div class="feedback-form-container">
            <div class="feedback-form-header">
                <div class="form-header-icon">✍️</div>
                <h2>Оставить отзыв</h2>
                <p>Поделитесь впечатлениями — это поможет нам стать лучше</p>
            </div>

            <form method="post" action="/feedback" class="feedback-form" id="feedbackForm">
                <div class="form-group">
                    <label for="author">
                        <span class="label-icon">👤</span>
                        Ваше имя или ник
                        <span class="required">*</span>
                    </label>
                    <input type="text" id="author" name="author"
                           value="{{form_data.get('author', '')}}"
                           placeholder="Например: Александр, MusicLover, 5opkaFan"
                           class="form-control {{'error' if errors.get('author') else ''}}"
                           autocomplete="off">
                    <div class="error-message">{{errors.get('author', '')}}</div>
                </div>

                <div class="form-group">
                    <label for="email">
                        <span class="label-icon">✉️</span>
                        Email
                        <span class="required">*</span>
                    </label>
                    <input type="email" id="email" name="email"
                           value="{{form_data.get('email', '')}}"
                           placeholder="example@mail.ru"
                           class="form-control {{'error' if errors.get('email') else ''}}"
                           autocomplete="off">
                    <div class="error-message">{{errors.get('email', '')}}</div>
                </div>

                <div class="form-group">
                    <label for="text">
                        <span class="label-icon">💬</span>
                        Текст отзыва
                        <span class="required">*</span>
                    </label>
                    <textarea id="text" name="text" rows="5"
                              placeholder="Расскажите, что вам понравилось, а что можно улучшить..."
                              class="form-control {{'error' if errors.get('text') else ''}}">{{form_data.get('text', '')}}</textarea>
                    <div class="error-message">{{errors.get('text', '')}}</div>
                    <div class="textarea-hint">
                        <span>ℹ️</span> Минимум 5 символов. Будьте вежливы 😊
                    </div>
                </div>

                <button type="submit" class="submit-btn">
                    <span class="btn-text">Отправить отзыв</span>
                    <span class="btn-icon">→</span>
                </button>
            </form>
        </div>
    </div>

    <!-- Список отзывов -->
    <div class="feedback-list-section">
        <div class="feedback-list-header">
            <h2>
                <span class="header-icon">💭</span>
                Отзывы слушателей
            </h2>
            <div class="feedback-count">
                <span class="count-number">{{len(feedbacks)}}</span>
                <span class="count-text">
                    % if len(feedbacks) == 1:
                        отзыв
                    % elif 2 <= len(feedbacks) <= 4:
                        отзыва
                    % else:
                        отзывов
                    % end
                </span>
            </div>
        </div>

        <div class="feedback-grid">
            % if not feedbacks:
                <div class="empty-state">
                    <div class="empty-state-icon">📝</div>
                    <h3>Пока нет отзывов</h3>
                    <p>Будьте первым, кто оставит отзыв!</p>
                </div>
            % else:
                % for index, fb in enumerate(feedbacks):
                    <div class="feedback-card" data-id="{{fb.get('id', index)}}">
                        <div class="feedback-card-header">
                            <div class="author-info">
                                <div class="author-avatar" style="background: linear-gradient(135deg, #667eea, #764ba2);">
                                    {{fb['author'][0].upper() if fb['author'] else '?'}}
                                </div>
                                <div class="author-details">
                                    <div class="author-name">{{fb['author']}}</div>
                                    <div class="feedback-date">
                                        <svg class="date-icon" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                                            <line x1="16" y1="2" x2="16" y2="6"></line>
                                            <line x1="8" y1="2" x2="8" y2="6"></line>
                                            <line x1="3" y1="10" x2="21" y2="10"></line>
                                        </svg>
                                        {{fb['date']}}
                                    </div>
                                    % if fb.get('email'):
                                        <div style="font-size: 10px; color: #999; margin-top: 4px;">
                                            ✉️ {{fb['email']}}
                                        </div>
                                    % end
                                </div>
                            </div>
                        </div>
                        <div class="feedback-card-body">
                            <p class="feedback-text">{{fb['text']}}</p>
                        </div>
                        <div class="feedback-card-footer">
                            <div class="feedback-rating">
                                <span class="rating-star">★</span>
                                <span class="rating-star">★</span>
                                <span class="rating-star">★</span>
                                <span class="rating-star">★</span>
                                <span class="rating-star">★</span>
                            </div>
                            <div class="feedback-like" onclick="toggleLike(this)">
                                <span class="like-icon">❤️</span>
                                <span class="like-count">0</span>
                            </div>
                        </div>
                    </div>
                % end
            % end
        </div>
    </div>
</div>

<script>
    // Анимация отправки формы
    document.getElementById('feedbackForm')?.addEventListener('submit', function(e) {
        const btn = this.querySelector('.submit-btn');
        const originalText = btn.innerHTML;
        btn.style.opacity = '0.7';
        btn.innerHTML = '<span class="btn-text">Отправляем...</span><span class="btn-icon">⏳</span>';

        setTimeout(() => {
            if (btn.style.opacity === '0.7') {
                btn.style.opacity = '1';
                btn.innerHTML = originalText;
            }
        }, 2000);
    });

    // Функция лайков
    function toggleLike(element) {
        const likeCount = element.querySelector('.like-count');
        let count = parseInt(likeCount.textContent);
        const heart = element.querySelector('.like-icon');

        if (element.classList.contains('liked')) {
            count--;
            element.classList.remove('liked');
            heart.style.transform = 'scale(1)';
        } else {
            count++;
            element.classList.add('liked');
            heart.style.transform = 'scale(1.2)';
            setTimeout(() => {
                heart.style.transform = 'scale(1)';
            }, 200);
        }
        likeCount.textContent = count;
    }

    // Анимация появления карточек при скролле
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.feedback-card').forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = `all 0.5s cubic-bezier(0.4, 0, 0.2, 1) ${index * 0.1}s`;
        observer.observe(card);
    });
</script>