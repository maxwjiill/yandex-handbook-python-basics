"""module task_d"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 > n2 and n1 > n3 and n2 > n3:
    print("1. Петя", "2. Вася", "3. Толя", sep="\n")
elif n1 > n2 and n1 > n3 and n2 < n3:
    print("1. Петя", "2. Толя", "3. Вася", sep="\n")
elif n2 > n1 and n2 > n3 and n1 > n3:
    print("1. Вася", "2. Петя", "3. Толя", sep="\n")
elif n2 > n1 and n2 > n3 and n1 < n3:
    print("1. Вася", "2. Толя", "3. Петя", sep="\n")
elif n3 > n1 and n3 > n2 and n1 > n2:
    print("1. Толя", "2. Петя", "3. Вася", sep="\n")
elif n3 > n1 and n3 > n2 and n1 < n2:
    print("1. Толя", "2. Вася", "3. Петя", sep="\n")
