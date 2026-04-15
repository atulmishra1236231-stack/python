l = [34, 43, 12, 34, 567]

# index = 0
# for item in l:
#     print(f"the item number at index {index} is {item}")
#     index +=1

#the above code can be simplified by using enumerate function

for index, item in enumerate(l):
    print(f"the item number at index {index} is {item}")