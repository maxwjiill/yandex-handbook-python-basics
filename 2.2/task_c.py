"""module task_c"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n3 > n1 and n3 > n2:
    print("Толя")
elif n1 > n2 and n1 > n3:
    print("Петя")
else:
    print("Вася")
