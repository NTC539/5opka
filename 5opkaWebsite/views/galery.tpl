% rebase('layout.tpl', title='Галерея', year=2026)

<!-- Верхняя навигация (если нужно дублировать, как в Figma) -->
<div style="max-width: 1200px; margin: 20px auto; padding: 0 20px;">
    <div style="display: flex; gap: 30px; justify-content: center;">
        <span style="font-size: 18px; color: #666;">Главная</span>
        <span style="font-size: 18px; color: #666;">Новости</span>
        <span style="font-size: 18px; color: #666;">Карьера</span>
        <span style="font-size: 18px; color: #666;">Музыка</span>
        <span style="font-size: 18px; color: #4CAF50; font-weight: bold;">Галерея</span>
    </div>
</div>

<!-- Основной контент -->
<div style="max-width: 1200px; margin: 0 auto; padding: 40px 20px;">

    <!-- Биография -->
    <div style="margin-bottom: 60px;">
        <h1 style="font-size: 36px; margin-bottom: 30px; font-weight: bold; color: #000;">Кирилл Александрович Баранов</h1>

        <div>
            <p style="margin-bottom: 20px; line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
                Родился 5 апреля 1996 года, проживает в Ростове-на-Дону. С 2011 года ведёт канал на YouTube под названием Пятёрка, на который подписано более 900 тысяч человек. До 2023—2024 года регулярно снимал видео о своих похождениях в игре Minecraft, которые собирали от десятков до сотен тысяч просмотров. Наибольшую популярность имеют его видео музыкальной направленности, например «MellSher, 5opka — Киношка».
            </p>
            <p style="margin-bottom: 20px; line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
                Раньше он презирал платформу Twitch из-за её правил в отношении запрещённых слов. В 2021 году он начал запускать трансляции одновременно и на Твиче, и на Ютубе. В последние годы он перестал запускать на Ютубе из-за ненадобности. Последняя трансляция на ютубе была в 2024 году.
            </p>
        </div>
    </div>

    <!-- Новости Пятёрки (если есть в галерее) -->
    <div style="margin-bottom: 60px;">
        <h2 style="font-size: 28px; margin-bottom: 30px; font-weight: bold;">Новости Пятёрки</h2>

        <div style="margin-bottom: 40px;">
            <div style="color: #999; font-size: 16px; margin-bottom: 10px;">20.02.2026</div>
            <p style="line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
                Значимость этих проблем настолько очевидна, что дальнейшее развитие различных форм деятельности обеспечивает актуальность вывода текущих активов. Безусловно, курс на социально-ориентированный национальный проект не даёт нам иного выбора, кроме определения приоретизации разума над эмоциями.
            </p>
        </div>

        <div style="margin-bottom: 40px;">
            <div style="color: #999; font-size: 16px; margin-bottom: 10px;">20.02.2026</div>
            <p style="line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
                Имеется спорная точка зрения, гласящая примерно следующее: сделанные на базе интернет-аналитики выводы набирают популярность среди определенных слоев населения, а значит, должны быть объективно рассмотрены соответствующими инстанциями.
            </p>
        </div>
    </div>

    <!-- Популярные треки (если есть в галерее) -->
    <div style="margin-bottom: 60px;">
        <h2 style="font-size: 28px; margin-bottom: 30px; font-weight: bold;">Популярные треки</h2>

        <div style="display: grid; gap: 15px;">
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 18px;">Жми Share</span>
                <span style="color: #999;">5opka</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 18px;">42</span>
                <span style="color: #999;">5opka, 6055</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 18px;">Веном Boy</span>
                <span style="color: #999;">Дмитрий Маликов, 5opka</span>
            </div>
            <div style="display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #eee;">
                <span style="font-size: 18px;">1000 жизней</span>
                <span style="color: #999;">5opka</span>
            </div>
        </div>
    </div>

    <!-- СП (Страна Подписчиков) -->
    <div style="margin-bottom: 60px;">
        <h2 style="font-size: 28px; margin-bottom: 20px; font-weight: bold;">СП (Страна Подписчиков)</h2>
        <p style="margin-bottom: 20px; line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
            СП — это платный сервер 5opka в игре Minecraft. Суть сервера в том, что в игре создается виртуальная страна с президентом, городами, политикой, правилами, законами. На серверах часто проводятся различные события и мероприятия. У сезонов серверов есть свой сюжет. На момент конца февраля 2026 года существует всего 5 сезонов: СП1, СП2 и т.д.
        </p>
        <p style="margin-bottom: 20px; line-height: 1.8; font-size: 18px; color: rgba(0,0,0,0.8);">
            Также помимо оригинального СП существуют дополнительные сервера:
        </p>
        <ul style="margin-left: 40px; margin-bottom: 20px;">
            <li style="margin-bottom: 10px; font-size: 18px;">СПм (Страна подписчиков мини)</li>
            <li style="margin-bottom: 10px; font-size: 18px;">spworlds</li>
            <li style="margin-bottom: 10px; font-size: 18px;">СПб (Страна подписчиков бедрок)</li>
        </ul>
    </div>

    <!-- Заголовки 1-4 -->
    <div style="margin-bottom: 60px;">
        <h2 style="font-size: 28px; margin: 30px 0 15px; font-weight: bold;">Заголовок 1</h2>
        <h2 style="font-size: 28px; margin: 30px 0 15px; font-weight: bold;">Заголовок 2</h2>
        <h2 style="font-size: 28px; margin: 30px 0 15px; font-weight: bold;">Заголовок 3</h2>
        <h2 style="font-size: 28px; margin: 30px 0 15px; font-weight: bold;">Заголовок 4</h2>
    </div>

    <!-- Нижняя навигация -->
    <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 15px; background-color: #F9F9F9; padding: 40px 20px; border-radius: 20px; margin-top: 60px;">
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; background-color: white; border-radius: 10px; cursor: pointer;">
            <span style="font-size: 18px;">Главная</span>
            <span style="font-size: 20px; color: #4CAF50;">→</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; background-color: white; border-radius: 10px; cursor: pointer;">
            <span style="font-size: 18px;">Новости</span>
            <span style="font-size: 20px; color: #4CAF50;">→</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; background-color: white; border-radius: 10px; cursor: pointer;">
            <span style="font-size: 18px;">Карьера</span>
            <span style="font-size: 20px; color: #4CAF50;">→</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; background-color: white; border-radius: 10px; cursor: pointer;">
            <span style="font-size: 18px;">Музыка</span>
            <span style="font-size: 20px; color: #4CAF50;">→</span>
        </div>
        <div style="display: flex; align-items: center; justify-content: space-between; padding: 15px 20px; background-color: white; border-radius: 10px; cursor: pointer;">
            <span style="font-size: 18px;">Галерея</span>
            <span style="font-size: 20px; color: #4CAF50;">→</span>
        </div>
    </div>
</div>