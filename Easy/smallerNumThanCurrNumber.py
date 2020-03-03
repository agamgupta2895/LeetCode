numners = [8, 1, 2, 2, 3]
y = sorted(numners)

res = []
result = {}
for index, num in enumerate(y):
    if num not in result:
        result[num] = index
for i in numners:
    res.append(result[i])
print(res)
