% rebase('layout.tpl', title=title, year=year)
<link rel="stylesheet" type="text/css" href="/static/content/shop.css"/>
<div>
	<div class="products-container">
        <div class="product-card" data-product="Футболка">
            <img src="/static/images/shopPage/T-Shirt.png" class="product-image" alt="Футболка"/>
            <h3 class="product-name">Футболка "42 братуха"</h3>
            <p class="product-desc">95% хлопок 5% лайкра</p>
            <p class="product-price">3 500 ₽</p>
        </div>
        <div class="product-card" data-product="Кружка">
            <img src="/static/images/shopPage/T-Shirt1.png" class="product-image" alt="Футболка"/>
            <h3 class="product-name">Футболка "Мачо и ботан"</h3>
            <p class="product-desc">95% хлопок 5% лайкра</p>
            <p class="product-price">3 500 ₽</p>
        </div>
        <div class="product-card" data-product="Фото с автографом">
            <img src="/static/images/shopPage/Calendar.png" class="product-image" alt="Календарь"/>
            <h3 class="product-name">Календарь 2026 (маленький)</h3>
            <p class="product-desc">200х100х85мм</p>
            <p class="product-price">800 ₽</p>
        </div>
    </div>
	<div class="form-container">
		<form action="/order" class="order-form" name="shop-order" method="post">
			<label for="order-first-name">Имя</label>
			<input id="order-first-name" type="text" name="first_name" placeholder="Введите ваше имя"/>
    
			<label for="order-last-name">Фамилия</label>
			<input id="order-last-name" type="text" name="last_name" placeholder="Введите вашу фамилию"/>

			<label for="order-phone-number">Номер телефона</label>
			<input id="order-phone-number" type="tel" name="phone_number" placeholder="Введите ваш номер телефона"/>
    
			<label for="order-email">Почта</label>
			<input id="order-email" type="email" name="email" placeholder="Введите вашу почту"/>

			<label for="order-address">Адрес доставки</label>
			<input id="order-address" type="text" name="address" placeholder="Введите адрес доставки"/>

			<label for="order-product">Товар</label>
            <select id="order-product" name="product">
                <option value="">Футболка "42 братуха"</option>
                <option value="">Футболка "Мачо и ботан"</option>
                <option value="">Календарь 2026 (маленький)</option>
            </select>
			<input id="order-submit" type="submit" name="submit" value="Заказать"/>
		</form>
	</div>
</div>