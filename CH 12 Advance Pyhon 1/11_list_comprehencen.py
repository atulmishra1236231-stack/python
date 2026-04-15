myList = [12, 2, 34, 1, 3, 6]

# squareList = []
# for item in myList:
#     squareList.append(item*item)

# print(squareList)

# the above code can be simplify by using list comprehencen

squareList = [i*i for i in myList]

print(squareList)