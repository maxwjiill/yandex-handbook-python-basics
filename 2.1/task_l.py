"""module task_l"""

n1 = int(input())
n2 = int(input())

print((n1 // 100 + n2 // 100) % 10, (n1 // 10 + n2 // 10) % 10, (n1 + n2) % 10, sep='')
