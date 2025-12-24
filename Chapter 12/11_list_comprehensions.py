myList = [1,2, 5, 8, 10]

# squaredList = []
# for item in myList:
#     squaredList.append(item**item)

squaredList = [item**item for item in myList]
print(squaredList)