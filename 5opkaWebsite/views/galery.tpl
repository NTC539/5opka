% rebase('layout.tpl', title='Галерея', year=2026)

<!-- Основной контейнер галереи -->
<div class="gallery-page">

    <!-- Заголовок 3 (как в вашем скриншоте) -->
    <h1 class="heading-text gallery-main-title">Заголовок 3</h1>

    <!-- Биография (текст из ТЗ) -->
    <div class="gallery-section">
        <p class="regular-text">
            Родился 5 апреля 1996 года, проживает в Ростове-на-Дону. С 2011 года ведёт канал на YouTube под названием Пятёрка, на который подписано более 900 тысяч человек. До 2023 —2024 года регулярно снимал видео о своих похождениях в игре Minecraft, которые собирали от десятков до сотен тысяч просмотров. Наибольшую популярность имеют его видео музыкальной направленности, например «MellSher, 5opka — Киношка».
        </p>
        <p class="regular-text">
            Раньше он презервал платформу Twitch из-за её правил в отношении запрещённых слов. В 2021 году он начал запускать трансляции одновременно и на Твиче, и на Ютубе. В последние годы он перестал запускать на Ютубе из-за ненадобности. Последняя трансляция на югубе была в 2024 году.
        </p>
    </div>

    <!-- Заголовки 1-4 -->
    <div class="gallery-section">
        <h2 class="heading-text gallery-subtitle">Заголовок 1</h2>
        <h2 class="heading-text gallery-subtitle">Заголовок 2</h2>
        <h2 class="heading-text gallery-subtitle">Заголовок 3</h2>
        <h2 class="heading-text gallery-subtitle">Заголовок 4</h2>
    </div>

    <!-- СП (Страна Подписчиков) -->
    <div class="gallery-section">
        <h2 class="heading-text">СП (Страна Подписчиков)</h2>
        <p class="regular-text">
            СП (Страна Подписчиков) — это платный сервер Sorbia в игре Minecraft. Суть сервера в том, что в игре создаются виртуальная страна с президентом, городами, политикой, правилами, законами. На серверах часто проводится различные события и мероприятия. У сезонов сервера есть свой окоп. На момент конца февраля 2026 года существует всего 5 сезонов: СП1, СП2 и т. д.
        </p>
        <p class="regular-text">
            Также помимо оригинального СП существуют дополнительные сервера:
        </p>
        <ul class="regular-text gallery-list">
            <li>СПм (Страна подписчиков мини)</li>
            <li>крипто</li>
            <li>СПб (страна подписчиков бейдж)</li>
        </ul>
    </div>

    <!-- ГАЛЕРЕЯ ИЗОБРАЖЕНИЙ (Сетка 3x3) -->
    <div class="gallery-grid-section">
        <h2 class="heading-text">Фотографии</h2>
        <div class="gallery-grid">
            <!-- Ряд 1: Картинки из папки career/1996/ -->
            <div class="gallery-grid-item">
                <img src="/static/images/career/1996/y1996-5opkaBarin.jpg" alt="5opka 1996">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/career/1996/y1996-5opkaGroup.png" alt="5opka group 1996">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/career/2011/y2011-bobHavalnik.png" alt="Bob Havalnik">
            </div>
            <!-- Ряд 2: Картинки из career/2011/ и musicPage/ -->
            <div class="gallery-grid-item">
                <img src="/static/images/career/2011/y2011-spworlds.jpg" alt="SPWorlds 2011">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/career/2011/y2011-willBeMineconInRussia.png" alt="Minecon Russia">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/musicPage/1000zhizneyImage.png" alt="1000 жизней">
            </div>
            <!-- Ряд 3: Картинки из musicPage/ и newsPage/ -->
            <div class="gallery-grid-item">
                <img src="/static/images/musicPage/42Image.png" alt="42">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/musicPage/zhmiShareImage.png" alt="Жми Share">
            </div>
            <div class="gallery-grid-item">
                <img src="/static/images/newsPage/placeholder132x132.png" alt="Placeholder">
            </div>
        </div>
    </div>

    <!-- Нижняя навигация (как в макете) -->
    <div class="gallery-footer-nav">
        <span class="regular-text">Главная</span>
        <span class="regular-text">Новости</span>
        <span class="regular-text">Карьера</span>
        <span class="regular-text">Музыка</span>
        <span class="regular-text gallery-nav-active">Галерея</span>
    </div>

</div>