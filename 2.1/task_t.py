"""module task_t"""

n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

# n = x + y -> x = n - y

# n * m = x * k1 + y * k2 -> n * m = (n - y) * k1 + y * k2

# k1 * n - k1 * y * + y * k2 = n * m

y = (k1 * n - n * m) // (k1 - k2)
x = n - y

print(x, y)
