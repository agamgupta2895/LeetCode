g = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

count = 0


for l in g:
    for num in l:
        if num < 0:
            count += 1

print(count)