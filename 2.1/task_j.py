"""module task_j"""

children_name = input()
wardrobe_number = input()

text = (
    f'Группа №{wardrobe_number[0]}.\n'
    f'{wardrobe_number[2]}. {children_name}.\n'
    f'Шкафчик: {wardrobe_number}.\n'
    f'Кроватка: {wardrobe_number[1]}.'
)

print(text)
