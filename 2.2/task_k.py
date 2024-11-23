"""module task_k"""

number = int(input())

n1 = number // 100 % 10
n2 = number // 10 % 10
n3 = number % 10

min_number = min(n1, n2, n3)
max_number = max(n1, n2, n3)

if min_number + max_number == ((n1 + n2 + n3) - (min_number + max_number)) * 2:
    print("YES")
else:
    print("NO")
