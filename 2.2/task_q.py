"""module task_q"""

a = float(input())
b = float(input())
c = float(input())

if a == b == c == 0:
    print("Infinite solutions")
elif a == b == 0 and c != 0:
    print("No solution")
elif a == 0:
    x = -c / b
    print(f"{x:.2f}")
else:

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        print("No solution")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    elif discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print(f"{min(x1, x2):.2f}", f"{max(x1, x2):.2f}")
