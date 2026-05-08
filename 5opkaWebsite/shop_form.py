import re
import os
import json
from bottle import post, get, request, template, response
from datetime import date

STR_REGEX = r'^[a-zA-Zа-яА-ЯёЁ]+$'
PHONE_REGEX = r'^(\+7|8)\d{10}$'

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

@post('/order', method='post')
def shop_form():
    first_name = request.forms.get('first_name').strip()
    last_name = request.forms.get('last_name').strip()
    phone_number = request.forms.get('phone_number').strip()
    email = request.forms.get('email').strip()
    address = request.forms.get('address').strip()
    product = request.forms.get('product').strip()
    order_date = str(date.today())

    if not first_name or not last_name or not phone_number or not email or not address or not product:
        return "<strong>Ошибка:</strong> Не все поля заполнены! <br/> <a href='/shop'>Назад</a>"
    if not re.match(STR_REGEX, first_name):
        return "<strong>Ошибка:</strong> Неверный формат имени! Используйте только символы кириллицы или латиницы.<br/> <a href='/shop'>Назад</a>"
    if not re.match(STR_REGEX, last_name):
        return "<strong>Ошибка:</strong> Неверный формат фамилии! Используйте только символы кириллицы или латиницы.<br/> <a href='/shop'>Назад</a>"
    if not re.match(PHONE_REGEX, phone_number):
        return "<strong>Ошибка:</strong> Неверный формат номера телефона! Используйте только цифры. Разрешены только российские номера, которые начинаются на +7 или 8.<br/> <a href='/shop'>Назад</a>"
    if len(address) < 10:
        return "<strong>Ошибка:</strong> Неверный формат номера адреса доставки! Используйте только цифры. Введите точный адрес доставки, чтобы мы могли доставить товар.<br/> <a href='/shop'>Назад</a>"
    
    orders = load_orders()
    
    if email not in orders:
            orders[email] = []
    orders[email].append([first_name, last_name, phone_number, address, product, order_date])
    with open('Orders.txt', 'w', encoding='utf-8') as outfile:
        json.dump(orders, outfile, indent=2, ensure_ascii=False)
    
    response.content_type = 'text/html; charset=utf-8'
    return template('shop/order_result.tpl', 
                    title="Заказ", 
                    year=2026, 
                    full_name=first_name + ' ' + last_name,
                    product = product,
                    address = address,
                    time=order_date)


@get('/shop')          
def shop_page():
    response.content_type = 'text/html; charset=utf-8'
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
    
    return template('shop',
                    title='Магазин',
                    year=2026,
                    orders=all_orders)



