% rebase('layout.tpl', title=title, year=year)
<link rel="stylesheet" type="text/css" href="/static/content/shop.css"/>
<div>
	<div class="products-container">
        <div class="product-card" data-product="Футболка">
            <img src="/static/images/shopPage/T-Shirt.png" class="product-image" alt="Футболка"/>
            <p class="product-name">Футболка "42 братуха"</p>
            <p class="product-desc">95% хлопок 5% лайкра</p>
            <p class="product-price">3 500 ₽</p>
        </div>
        <div class="product-card" data-product="Кружка">
            <img src="/static/images/shopPage/T-Shirt1.png" class="product-image" alt="Футболка"/>
            <p class="product-name">Футболка "Мачо и ботан"</p>
            <p class="product-desc">95% хлопок 5% лайкра</p>
            <p class="product-price">3 500 ₽</p>
        </div>
        <div class="product-card" data-product="Фото с автографом">
            <img src="/static/images/shopPage/Calendar.png" class="product-image" alt="Календарь"/>
            <p class="product-name">Календарь 2026 (маленький)</p>
            <p class="product-desc">200х100х85мм</p>
            <p class="product-price">800 ₽</p>
        </div>
    </div>
	<div class="form-container">
		<form action="/order" class="order-form" name="shop-order" method="post">
			<!-- Имя -->
            <label for="order-first-name">Имя</label>
            <input id="order-first-name" type="text" name="first_name"
                   placeholder="Введите ваше имя"
                   value="{{ form_data.get('first_name', '') if form_data else '' }}"
                   class="{{ 'error-input' if errors and 'first_name' in errors else '' }}">
            % if errors and 'first_name' in errors:
                <span class="error-msg">{{ errors['first_name'] }}</span>
            % end

            <!-- Фамилия -->
            <label for="order-last-name">Фамилия</label>
            <input id="order-last-name" type="text" name="last_name"
                   placeholder="Введите вашу фамилию"
                   value="{{ form_data.get('last_name', '') if form_data else '' }}"
                   class="{{ 'error-input' if errors and 'last_name' in errors else '' }}">
            % if errors and 'last_name' in errors:
                <span class="error-msg">{{ errors['last_name'] }}</span>
            % end

            <!-- Телефон -->
            <label for="order-phone-number">Номер телефона</label>
            <input id="order-phone-number" type="tel" name="phone_number"
                   placeholder="Введите ваш номер телефона"
                   value="{{ form_data.get('phone_number', '') if form_data else '' }}"
                   class="{{ 'error-input' if errors and 'phone_number' in errors else '' }}">
            % if errors and 'phone_number' in errors:
                <span class="error-msg">{{ errors['phone_number'] }}</span>
            % end

            <!-- Email -->
            <label for="order-email">Почта</label>
            <input id="order-email" type="email" name="email"
                   placeholder="Введите вашу почту"
                   value="{{ form_data.get('email', '') if form_data else '' }}"
                   class="{{ 'error-input' if errors and 'email' in errors else '' }}">
            % if errors and 'email' in errors:
                <span class="error-msg">{{ errors['email'] }}</span>
            % end

            <!-- Адрес -->
            <label for="order-address">Адрес доставки</label>
            <input id="order-address" type="text" name="address"
                   placeholder="Введите адрес доставки"
                   value="{{ form_data.get('address', '') if form_data else '' }}"
                   class="{{ 'error-input' if errors and 'address' in errors else '' }}">
            % if errors and 'address' in errors:
                <span class="error-msg">{{ errors['address'] }}</span>
            % end

            <!-- Товар -->
            <label for="order-product">Товар</label>
            <select id="order-product" name="product"
                    class="{{ 'error-input' if errors and 'product' in errors else '' }}">
                <option value="">-- Выберите --</option>
                <option value='Футболка "42 братуха"'
                    % if form_data and form_data.get('product') == 'Футболка "42 братуха"':
                        selected
                    % end
                >Футболка "42 братуха"</option>
                <option value='Футболка "Мачо и ботан"'
                    % if form_data and form_data.get('product') == 'Футболка "Мачо и ботан"':
                        selected
                    % end
                >Футболка "Мачо и ботан"</option>
                <option value="Календарь 2026 (маленький)"
                    % if form_data and form_data.get('product') == 'Календарь 2026 (маленький)':
                        selected
                    % end
                >Календарь 2026 (маленький)</option>
            </select>
            % if errors and 'product' in errors:
                <span class="error-msg">{{ errors['product'] }}</span>
            % end
			<input id="order-submit" type="submit" name="submit" value="Заказать"/>
		</form>
	</div>
    <div class="orders-container">
        <h1>У нас уже заказали</h1>
        % if orders:
            % for order in orders:
            <div class="order-card">
                <div class="order-card-avatar">
                    <span>{{ order['full_name'][0] }}</span>
                </div>
                <div class="order-card-info">
                    <p class="order-fullname">{{ order['full_name'] }}</p>
                    <p class="order-product">{{ order['product'] }}</p>
                    <p class="order-price">{{ order['price'] }} ₽</p>
                    <p class="order-date">{{ order['date'] }}</p>
                </div>
            </div>
            % end
        % else:
            <p>Пока заказов нет. Станьте первым!</p>
        % end
    </div>
</div>