S = "ZZZZZZ"
J=  "z"

ob = {}

for elem in S:
    if elem in ob:
        ob[elem] = ob[elem] + 1
    else:
        ob[elem]= 1
res = 0
for jewel in J:
    if jewel in ob:
        res  = res + ob[jewel]

print(res)