"""module task_f"""

name = input()
price = int(input())
weight = int(input())
amount = int(input())
paycheck = (
    'Чек\n'
    f'{name} - {weight}кг - {price}руб/кг\n'
    f'Итого: {price * weight}руб\n'
    f'Внесено: {amount}руб\n'
    f'Сдача: {amount - weight * price}руб\n'
)
print(paycheck)
