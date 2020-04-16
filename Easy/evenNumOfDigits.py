num = [555,901,482,1771]
res = 0
for element in num:
    if len(str(element)) % 2 == 0:
        res = res+1
print(res)
