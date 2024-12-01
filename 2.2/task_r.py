"""module task_r"""

a = int(input())
b = int(input())
c = int(input())

min_side = min(a, b, c)
max_side = max(a, b, c)
othr_side = ((a + b + c) - min_side - max_side)

if max_side ** 2 < min_side ** 2 + othr_side ** 2:
    print("крайне мала")
elif max_side ** 2 > min_side ** 2 + othr_side ** 2:
    print("велика")
else:
    print("100%")
