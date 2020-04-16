num = 9969

res = [int(x) for x in str(num)]

for i, val in enumerate(res):
    if val == 6:
        res[i] = 9
        break

r = int("".join(map(str, res)))

print(r)
