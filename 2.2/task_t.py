"""module task_t"""

s1 = input()
s2 = input()
s3 = input()

if "зайка" in s1 and "зайка" in s2 and "зайка" not in s3:
    if s1 < s2:
        print(s1, len(s1))
    else:
        print(s2, len(s2))
elif "зайка" in s1 and "зайка" not in s2 and "зайка" in s3:
    if s1 < s3:
        print(s1, len(s1))
    else:
        print(s3, len(s3))
elif "зайка" not in s1 and "зайка" in s2 and "зайка" in s3:
    if s2 < s3:
        print(s2, len(s2))
    else:
        print(s3, len(s3))
elif "зайка" in s1 and "зайка" not in s2 and "зайка" not in s3:
    print(s1, len(s1))
elif "зайка" not in s1 and "зайка" in s2 and "зайка" not in s3:
    print(s2, len(s2))
elif "зайка" not in s1 and "зайка" not in s2 and "зайка" in s3:
    print(s3, len(s3))
else:
    if s1 < s2 and s1 < s3:
        print(s1, len(s1))
    elif s2 < s1 and s2 < s3:
        print(s2, len(s2))
    elif s3 < s1 and s3 < s2:
        print(s3, len(s3))
