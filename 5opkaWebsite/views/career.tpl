% rebase('layout.tpl', title=title, year=year, timeline_data=timeline_data)

<h1>Career</h1>

<div class="container">
    <!-- Шапка -->
    <header class="header">
        <h1 class="heading-text">Кирилл "5opka" Баранов</h1>
        <p class="regular-text subtitle">Minecraft-стример, мем-лорд, создатель "42-братух" • Родился 5 апреля 1996</p>
    </header>

    <!-- Таймлайн -->
    <div class="nav-container">
        <div class="nav-header">
            <h2>Таймлайн жизни и карьеры</h2>
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