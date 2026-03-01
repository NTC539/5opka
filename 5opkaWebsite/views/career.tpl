% rebase('layout.tpl', title=title, year=year, timeline_data=timeline_data)

<script>
// Сохраняем позицию скролла при клике на точки таймлайна
document.addEventListener('click', function(e) {
    if (e.target.closest('.timeline-point')) {
        sessionStorage.setItem('scrollPosition', window.scrollY);
    }
});

// Восстанавливаем позицию после загрузки страницы
window.addEventListener('load', function() {
    const savedPosition = sessionStorage.getItem('scrollPosition');
    if (savedPosition) {
        window.scrollTo(0, parseInt(savedPosition));
        sessionStorage.removeItem('scrollPosition');
    }
});
</script>

<div class="container">
    <!-- Шапка -->
    <header class="header">
        <h1 class="heading-text">Кирилл "5opka" Баранов</h1>
        <p class="regular-text subtitle">Minecraft-стример, мем-лорд, создатель "42-братух"</p>
    </header>

    <!-- Таймлайн -->
    <div class="nav-container">
        <div class="nav-header regular-text">
            <h2 class=>Таймлайн жизни и карьеры</h2>
        </div>
          
        <div class="timeline">  
            <div class="timeline-line"></div>
            
            <div class="timeline-points">
                % for year, data in timeline_data.items():
                    <a href="/career/{{year}}" class="timeline-point {{'active' if year == selected_year else ''}}">
                        <div class="point-circle">
                            <span class="regular-text age">{{data['age']}}</span>
                        </div>
                        <div class="point-label">
                            <div class="regular-text year">{{year}}</div>
                            <div class="regular-text title">{{data['title']}}</div>
                        </div>
                    </a>
                % end
            </div>
        </div>
    </div>

    <!-- Контент выбранного года из отдельного файла -->
    {{!year_content}}
</div>