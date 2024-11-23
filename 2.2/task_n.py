"""module task_n"""

number = int(input())

n1 = number // 100 % 10
n2 = number // 10 % 10
n3 = number % 10

if n1 == 0:
    max_number = max(
        (n2 * 10 + n1),
        (n2 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )
    min_number = min(
        (n2 * 10 + n1),
        (n2 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )

    print(min_number, max_number)
elif n2 == 0:
    max_number = max(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )
    min_number = min(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )

    print(min_number, max_number)
elif n3 == 0:
    max_number = max(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n2 * 10 + n1),
        (n2 * 10 + n3)
    )
    min_number = min(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n2 * 10 + n1),
        (n2 * 10 + n3)
    )

    print(min_number, max_number)
else:
    max_number = max(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n2 * 10 + n1),
        (n2 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )
    min_number = min(
        (n1 * 10 + n2),
        (n1 * 10 + n3),
        (n2 * 10 + n1),
        (n2 * 10 + n3),
        (n3 * 10 + n1),
        (n3 * 10 + n2)
    )

    print(min_number, max_number)
