"""module task_p"""

n1 = int(input())
n2 = int(input())
n3 = int(input())

# n1 = 5
# n2 = 7
# n3 = 10

name_first = ""
name_second = ""
name_third = ""

if n1 > n2 and n1 > n3 and n2 > n3:
    name_first = "Петя"
    name_second = "Вася"
    name_third = "Толя"
elif n1 > n2 and n1 > n3 and n2 < n3:
    name_first = "Петя"
    name_second = "Толя"
    name_third = "Вася"
elif n2 > n1 and n2 > n3 and n1 > n3:
    name_first = "Вася"
    name_second = "Петя"
    name_third = "Толя"
elif n2 > n1 and n2 > n3 and n1 < n3:
    name_first = "Вася"
    name_second = "Толя"
    name_third = "Петя"
elif n3 > n1 and n3 > n2 and n1 > n2:
    name_first = "Толя"
    name_second = "Петя"
    name_third = "Вася"
elif n3 > n1 and n3 > n2 and n1 < n2:
    name_first = "Толя"
    name_second = "Вася"
    name_third = "Петя"

pedestal_message = (
    f"{name_first: ^{8 * 3}}\n"
    f"{name_second: ^{8}}\n"
    f"{name_third: ^{8 * 5}}\n"
    f"{"II": ^{8}}{"I": ^{8}}{"III": ^{8}}"
)

print(pedestal_message)
