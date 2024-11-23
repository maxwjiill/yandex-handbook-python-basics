"""module task_j"""

number = int(input())

first_part = (number % 10) + (number // 10 % 10)
second_part = (number // 10 % 10) + (number // 100 % 10)

if first_part > second_part:
    print(first_part, second_part, sep='')
else:
    print(second_part, first_part, sep='')
