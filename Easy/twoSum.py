# In an array find a pair with the sum X

size = int(input("Number of elements in an array"))

arr = {}
l = []
for i in range(0, size):
    elements = int(input("Enter the number"))
    l.append(elements)
    arr[elements] = -1

sum = int(input("Sum of the number "))

for index, element in enumerate(l):
    firstNum = element
    secondNum = sum - firstNum
    if secondNum in arr and arr[secondNum] != -1:
        print("Pair = ", firstNum, secondNum)
        print("index", index, arr[secondNum])
    else:
        arr[firstNum] = index
