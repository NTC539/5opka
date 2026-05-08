import re
import os
import json
from bottle import post, get, request, template, response
from datetime import date

STR_REGEX = r'^[a-zA-Zа-яА-ЯёЁ]+$'
PHONE_REGEX = r'^(\+7|8)\d{10}$'
EMAIL_REGEX = r'^(?=.{1,254}$)[a-zA-Z0-9.!#$%&\'*+/=?^_\\{|}~-]{1,64}@[a-zA-Z0-9.-]{1,}\.[a-zA-Z]{2,}$'

def is_email_format_correct(email):
    #По регулярному выражению проверям формат почты
    if not re.match(EMAIL_REGEX, email):
        return False
    #Дополнительно ищем невозможные комбинации точек и тире в почте
    elif ".." in email or email.startswith(".") or email.endswith(".") or ".@" in email or "@." in email:
        return False
    elif "@-" in email or "-@" in email or "-." in email or ".-" in email:
        return False
    return True

def is_name_valid(name):
    return bool(re.fullmatch(STR_REGEX, name))

def is_phone_valid(phone):
    return bool(re.fullmatch(PHONE_REGEX, phone))

def load_orders(filename='Orders.txt'): 
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except (json.JSONDecodeError, IOError):
        return {}

def get_shop_data():
    prices = {
        'Футболка "42 братуха"': 3500,
        'Футболка "Мачо и ботан"': 3500,
        'Календарь 2026 (маленький)': 800
    }
    orders = load_orders()
    all_orders = []
    for email, order_list in orders.items():
        for order in order_list:
            all_orders.append({
                'full_name': f"{order[0]} {order[1]}",
                'product': order[4],
                'price': prices.get(order[4], '—'),
                'date': order[5]
            })
    return all_orders

@post('/order')
def shop_form():
    # Считываем данные
    first_name = request.forms.getunicode('first_name').strip()
    last_name = request.forms.getunicode('last_name').strip()
    phone_number = request.forms.getunicode('phone_number').strip()
    email = request.forms.getunicode('email').strip()
    address = request.forms.getunicode('address').strip()
    product = request.forms.getunicode('product').strip()
    order_date = str(date.today())

    # Собираем ошибки
    errors = {}
    if not first_name:
        errors['first_name'] = 'Имя обязательно'
    elif not is_name_valid(first_name):
        errors['first_name'] = 'Используйте только буквы (русские или латинские)'

    if not last_name:
        errors['last_name'] = 'Фамилия обязательна'
    elif not is_name_valid(last_name):
        errors['last_name'] = 'Используйте только буквы (русские или латинские)'

    if not phone_number:
        errors['phone_number'] = 'Телефон обязателен'
    elif not is_phone_valid(phone_number):
        errors['phone_number'] = 'Формат: +7XXXXXXXXXX или 8XXXXXXXXXX (10 цифр)'

    if not email:
        errors['email'] = 'Почта обязательна'
    elif not is_email_format_correct(email):
        errors['email'] = 'Неверный формат почты'

    if not address:
        errors['address'] = 'Адрес обязателен'
    elif len(address) < 10:
        errors['address'] = 'Введите точный адрес (не менее 10 символов)'

    if not product:
        errors['product'] = 'Выберите товар'

    # Если есть ошибки — возвращаем ту же страницу с формой и ошибками
    if errors:
        all_orders = get_shop_data()
        response.content_type = 'text/html; charset=utf-8'
        return template('shop',
                        title='Магазин',
                        year=2026,
                        orders=all_orders,
                        errors=errors,
                        form_data={
                            'first_name': first_name,
                            'last_name': last_name,
                            'phone_number': phone_number,
                            'email': email,
                            'address': address,
                            'product': product
                        })

    # Ошибок нет — сохраняем заказ
    orders = load_orders()
    if email not in orders:
        orders[email] = []
    orders[email].append([first_name, last_name, phone_number, address, product, order_date])
    with open('Orders.txt', 'w', encoding='utf-8') as outfile:
        json.dump(orders, outfile, indent=2, ensure_ascii=False)

    response.content_type = 'text/html; charset=utf-8'
    return template('shop/order_result.tpl',
                    title="Заказ оформлен",
                    year=2026,
                    full_name=f"{first_name} {last_name}",
                    product=product,
                    address=address,
                    time=order_date)


@get('/shop')
def shop_page():
    all_orders = get_shop_data()              # ваша вспомогательная функция
    response.content_type = 'text/html; charset=utf-8'
    return template('shop',
                    title='Магазин',
                    year=2026,
                    orders=all_orders,
                    form_data={},             # всегда передаём пустой словарь
                    errors={})                # и пустой словарь ошибок



