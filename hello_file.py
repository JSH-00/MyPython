#!/usr/bin/python
# -*- coding: UTF-8 -*-
# coding = utf-8

# print("Hello word!")


# 写入文件
filename = "hello_file.txt"
with open(filename, 'w') as file_object:
    file_object.write("Add a word\n")
    file_object.write("Add two words A ")
    file_object.write("Add two words")

# 不用with读取文件
f = open("hello_file.txt", "r+")
f.write("aaa")                 # 覆盖原内容
print("光标位置：", f.tell())
print("文件名: ", f.name)
f.seek(0, 0)                   # 移动光标到开头
lines = f.read()
print("文件内容:\n", lines)
print("访问模式 : ", f.mode)
print("类型：", type(lines))
f.close()


# 修改文件内指定内容


def alter(filename2, old_str, new_str):
    filedata = ""
    with open(filename2, "r", encoding="utf-8") as file_change:
        for line in file_change:
            if old_str in line:
              #   print(line)
                line = line.replace(old_str, new_str)
            filedata += line
    with open(filename2, "w", encoding="utf-8") as file_change:
        file_change.write(filedata)


alter("hello_file.txt", "Add two words", "change")


# 遗留问题：rwa+的区别

# 光标移动