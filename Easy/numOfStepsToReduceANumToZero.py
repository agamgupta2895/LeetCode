num = 14
count = 0
while num != 0:
    count = count + 1
    if (num % 2 == 0):
        num = num // 2
    else:
        num = num - 1


print(count)