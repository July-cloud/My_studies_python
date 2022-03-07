#!/usr/bin/env python
# -*- coding: utf-8 -*-



goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}



store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе


lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
table_code = goods['Стол']
table_item = store[table_code][0]
table_quantity = table_item['quantity']
table_price = table_item['price']
table_code2 = goods['Стол']
table_item2 = store[table_code2][1]
table_quantity2 = table_item2['quantity']
table_price2 = table_item2['price']
all_quantity = table_quantity + table_quantity2
all_price = table_price + table_price2
table_cost = all_quantity * all_price
print('Стол -', all_quantity, 'шт, стоимость', table_cost, 'руб')


lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_quantity = sofa_item['quantity']
sofa_price = sofa_item['price']
sofa_code2 = goods['Диван']
sofa_item2 = store[sofa_code2][1]
sofa_quantity2 = sofa_item2['quantity']
sofa_price2 = sofa_item2['price']
all_quantity = sofa_quantity + sofa_quantity2
all_price = sofa_price + sofa_price2
sofa_cost = all_quantity * all_price
print('Диван -', all_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_quantity = chair_item['quantity']
chair_price = chair_item['price']
chair_code2 = goods['Стул']
chair_item2 = store[chair_code2][1]
chair_quantity2 = chair_item2['quantity']
chair_price2 = chair_item2['price']
chair_code3 = goods['Стул']
chair_item3 = store[chair_code3][2]
chair_quantity3 = chair_item3['quantity']
chair_price3 = chair_item3['price']
all_quantity = chair_quantity + chair_quantity2 + chair_quantity3
all_price = chair_price + chair_price2 + chair_price3
chair_cost = all_quantity * all_price
print('Стул -', all_quantity, 'шт, стоимость', chair_cost, 'руб')







