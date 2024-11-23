"""module task_l"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 + n2 > n3 and n3 + n2 > n1 and n1 + n3 > n2:
    print("YES")
else:
    print("NO")
