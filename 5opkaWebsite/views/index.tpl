% rebase('layout.tpl', title='Главная', year=2026)

<!-- Главная страница -->
<div class="home-page">

    <!-- Hero секция с цитатой -->
    <div class="home-hero">
        <div class="home-hero-image">
            <img src="/static/images/homePage/homeGreetingImage.png" alt="5opka">
        </div>
        <div class="home-hero-quote">
            <p class="regular-text">
                <em>
                    “Звонил бабушке, она оказывается тоже про бан знает.
                    Волнуется очень за меня, думает, что это конец карьеры.
                    Сказала позвонить ей, как только разбанят...”
                </em>
            </p>
            <span class="home-quote-author regular-text">© Кирилл Баранов</span>
        </div>
    </div>

    <!-- Основной род деятельности -->
    <div class="home-section">
        <h2 class="heading-text">Основной род деятельности</h2>
        <p class="regular-text">
            Кирилл Александрович Баранов — популярный российский видеоблогер, стример, исполнитель,
            делающий контент на YouTube и Twitch. Знаменит своими видео и стримам по игре Minecraft,
            эпатажными выходками на премиях и мероприятих, мему 42 братуха.
        </p>
    </div>

    <!-- Биография -->
    <div class="home-section">
        <h2 class="heading-text">Биография</h2>
        <p class="regular-text">
            Родился 5 апреля 1996 года, проживает в Ростове-на-Дону. С 2011 года ведёт канал на YouTube
            под названием Пятёрка, на который подписано более 900 тысяч человек. До 2023—2024 года
            регулярно снимал видео о своих похождениях в игре Minecraft, которые собирали от десятков
            до сотен тысяч просмотров. Наибольшую популярность имеют его видео музыкальной направленности,
            например «MellSher, 5opka — Киношка».
        </p>
        <p class="regular-text">
            Раньше он презирал платформу Twitch из-за её правил в отношении запрещённых слов. В 2021 году
            он начал запускать трансляции одновременно и на Твиче, и на Ютубе. В последние годы он перестал
            запускать на Ютубе из-за ненадобности. Последняя трансляция на ютубе была в 2024 году.
        </p>
    </div>

    <!-- Ряд изображений (3 картинки) -->
    <div class="home-image-row">
        <div class="home-image-item">
            <img src="/static/images/homePage/homeRowImage1.png" alt="5opka image 1">
        </div>
        <div class="home-image-item">
            <img src="/static/images/homePage/homeRowImage2.png" alt="5opka image 2">
        </div>
        <div class="home-image-item">
            <img src="/static/images/homePage/homeRowImage3.png" alt="5opka image 3">
        </div>
    </div>

    <!-- СП (Страна Подписчиков) -->
    <div class="home-section">
        <h2 class="heading-text">СП (Страна Подписчиков)</h2>
        <p class="regular-text">
            СП — это платный сервер 5opka в игре Minecraft. Суть сервера в том, что в игре создается
            виртуальная страна с президентом, городами, политикой, правилами, законами. На серверах
            часто проводятся различные события и мероприятия. У сезонов серверов есть свой сюжет.
            На момент конца февраля 2026 года существует всего 5 сезонов: СП1, СП2 и т.д.
        </p>
        <p class="regular-text">
            Также помимо оригинального СП существуют дополнительные сервера:
        </p>
        <ul class="regular-text home-list">
            <li>СПм (Страна подписчиков мини)</li>
            <li>spworlds</li>
            <li>СПб (Страна подписчиков бедрок)</li>
        </ul>
    </div>

        <!-- Форма обратной связи для лабораторной работы -->
    <div class="home-section">
    <h3>Ask a Question</h3>
    <form action="/home" method="post">
            <p>
            <input type="text"
                   size="50"
                   class="form-control"
                   name="USERNAME"
                   placeholder="Your name">
        </p>
        <p>
            <textarea rows="2"
                      cols="50"
                      style="resize: none;"
                      class="form-control"
                      name="QUEST"
                      placeholder="Your question"></textarea>
        </p>
        <p>
            <input type="text"
                   size="50"
                   class="form-control"
                   name="ADRESS"
                   placeholder="Your email">
        </p>
        <p>
            <input type="submit"
                   value="Send">
        </p>
    </form>
</div>

</div>