from bottle import post, request
from datetime import date

@post('/order', method='post')
def shop_form():
    first_name = request.forms.get('first_name').strip()
    last_name = request.forms.get('last_name').strip()
    phone_number = request.forms.get('phone_number').strip()
    email = request.forms.get('email').strip()
    address = request.forms.get('address').strip()
    product = request.forms.get('product').strip()

    return first_name + last_name + phone_number + email + address + product + str(date.today())



