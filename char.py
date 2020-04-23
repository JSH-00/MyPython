a = 10
b = 20
print(f"{a} * {b} = {a*b}")

a, b = 10, 30
print("{0} * {1} = {2}".format(a, b, a * b))

# 列表
list1 = [1, 3, 5, 7, 100]
for index in range(len(list1)):
    print(list1[index])

# print(range(len(list1))) # range(0, 5)

# for elem in list1:
#     print(elem)
#
# for index, elem in enumerate(list1):
#     print(index, elem)

list1.append(200)
list1.insert(2, 300)
for elem in list1:
    print(elem)