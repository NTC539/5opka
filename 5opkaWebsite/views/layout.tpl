<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Bottle Application</title>
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>

<body>
    <div>
        <div>
            <div class="navbar-layout">
                <ul class="navbar navbar-button-list">
                    <li><a href="/home">Главная</a></li>
                    <li><a href="/news">Новости</a></li>
                    <li><a href="/career">Карьера</a></li>
                    <li><a href="/music">Музыка</a></li>
                    <li><a href="/galery">Галерея</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div>
        {{!base}}
        <hr />
        <footer>
            <p>&copy; {{ year }} - Иван Езерский, Дмитрий Садеков, Георгий Мироненко</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
<!-- Краткая информация -->
<div class="about-preview">
    <div class="about-text">
        <h2 class="heading-text section-title">О проекте</h2>
        <p class="regular-text">
            Добро пожаловать на официальный сайт. Здесь вы найдете последние новости,
            информацию о творчестве, музыку и многое другое. Проект существует с 2020 года
            и продолжает развиваться.
        </p>

        <div class="about-stats">
            <div class="stat-item">
                <span class="stat-number">50+</span>
                <span class="stat-label regular-text">песен</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">100k</span>
                <span class="stat-label regular-text">слушателей</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">5</span>
                <span class="stat-label regular-text">альбомов</span>
            </div>
        </div>

        <a href="/about" class="read-more">Узнать больше</a>
    </div>

    <div class="about-image">
        <img src="/static/images/homePage/aboutImage.png" alt="О проекте">
    </div>
</div>