% rebase('layout.tpl', title=title, year=year)

<div class="container">
	<link rel="stylesheet" type="text/css" href="/static/content/shop.css"/>

	<form class="order-form" name="shop-order" method="post">
		
		<label for="order-first-name">Имя</label>
		<input id="order-first-name" type="text" name="first_name" placeholder="Введите ваше имя"/>
    
		<label for="order-last-name">Фамилия</label>
		<input id="order-last-name" type="text" name="last_name" placeholder="Введите вашу фамилию"/>
    
		<label for="order-email">Почта</label>
		<input id="order-email" type="email" name="email" placeholder="Введите вашу почту"/>

		<select id="order-product" name="product">
			<option balue="">Футболка</option>
			<option balue="">Кружка</option>
			<option balue="">Фото с автографом</option>
		</select>

		<input id="order-submit" type="submit" name="submit" value="Заказать">

		
		
		<label>
	</form>
</div>