"""module task_o"""

hour = int(input())
minute = int(input())
minutes = int(input())

current_minutes = hour * 60 + minute
future_minutes = current_minutes + minutes
minutes_day = 24 * 60

h1 = future_minutes - ((future_minutes // minutes_day) * minutes_day)

print(f"{h1 // 60:0>2}:{h1 % 60:0>2}")
