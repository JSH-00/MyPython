import sys
# a = 10
# b = 20
# print(f"{a} * {b} = {a*b}")
#
# a, b = 10, 30
# print("{0} * {1} = {2}".format(a, b, a * b))
#
# # 列表
# list1 = [1, 3, 5, 7, 100]
# for index in range(len(list1)):
#     print(list1[index])
#
# print(range(len(list1))) # range(0, 5)
#
# for elem in list1:
#     print(elem)
#
# for index, elem in enumerate(list1):
#     print(index, elem)
#
# list1.append(200)
# list1.insert(2, 300)
# for elem in list1:
#     print(elem)

# f = [x for x in range(1, 10)]
# print(f)
#
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
#

# ** 2 平方
# f = [x ** 2 for x in range(1, 1001)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)

# # 定义元组
# t= ("Suger", 20, True, "浙江杭州")
# # t[0] = "SS"


# class Foo():
#
#   def __init__(event):
#     print('This is method')
#
#   def public_method(event):
#     print('This is public method')
#
#   def __fullprivate_method(event):
#     print('This is fullprivate_method')
#
#   def _halfprivate_method(event):
#     print('This is halfprivate_method')
#
#
# f = Foo()
# f.public_method() # OK
# f._halfprivate_method() # OK
# # f.__fullprivate_method() # Error occur
# f._Foo__fullprivate_method() # OK  私有成员使用方法
