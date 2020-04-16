num = 4421
sum = 0
prod = 1
n = 0
while num > 0:
    n = num % 10
    sum = sum + n
    prod = prod * n
    num = num // 10
print(prod-sum)