"""module task_a"""

print("Как Вас зовут?")
name = input()

print(f"Здравствуйте, {name}!\nКак дела?")
answer = input()
if answer == "хорошо":
    print("Я за вас рада!")
elif answer == "плохо":
    print("Всё наладится!")
