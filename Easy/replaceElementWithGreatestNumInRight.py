nums = [17, 18, 5, 4, 6, 1]
out = [-1]
greatest = 0
for num in nums[::-1]:
    if greatest < num:
        greatest = num
    out.append(greatest)
out.pop()
print(out[::-1])