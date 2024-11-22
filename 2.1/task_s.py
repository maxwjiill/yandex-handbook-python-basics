"""module task_s"""

product_name = input()
product_price = int(input())
product_weight = int(input())
user_money = int(input())

total_price = product_price * product_weight
change = user_money - total_price

price_line = f"{product_weight}кг * {product_price}руб/кг"

message = (
    f"{'Чек':=^35}\n"
    f"{'Товар:': <{35 - len(product_name)}}{product_name}\n"
    f"{'Цена:': <{35 - len(price_line)}}{price_line}\n"
    f"{'Итого:': <{35 - len(f"{total_price}руб")}}{total_price}руб\n"
    f"{'Внесено:': <{35 - len(f"{user_money}руб")}}{user_money}руб\n"
    f"{'Сдача:': <{35 - len(f"{change}руб")}}{change}руб\n"
    f"{'=' * 35}"
)

print(message)
