"""module task_o"""

n1 = int(input())
n2 = int(input())

max_n = max(n1 // 10 % 10, n1 % 10, n2 // 10 % 10, n2 % 10)
min_n = min(n1 // 10 % 10, n1 % 10, n2 // 10 % 10, n2 % 10)
othr_n = (((n1 // 10 % 10) + (n1 % 10) + (n2 // 10 % 10) + (n2 % 10)) - max_n - min_n) % 10

print(max_n, othr_n, min_n, sep='')
