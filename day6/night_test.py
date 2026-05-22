# def write_one():
#     fw = open("./document/test.txt", "w",encoding="utf-8")
#     fw.write("hello world\n")
#     fw.write("hello atguigu\n")
#     fw.close()
#
# def write_two():
#     fw = open("./document/test.txt", "w",encoding="utf-8")
#     fw.write("你好，世界\n")
#     fw.write("你好，尚硅谷\n")
#     fw.close()
#
# # write_one()
# write_two()
#
# def write_append():
#     fw = open("./document/test.txt", "a",encoding="utf-8")
#     fw.write("python\n")
#     fw.write("ai\n")
#     fw.close()
#
# write_append()


print("一次读取所有行，返回列表".center(50, "-"))
fr = open("document/test.txt", "r", encoding="utf-8")
print(fr.readlines())
fr.close()

print("一次读取一行或多行".center(50, "-"))
fr = open("document/test.txt", "r", encoding="utf-8")
print(fr.readlines(3)) # 读取3个字符所在的行
fr.close()
435
print("一次读取一行或多行".center(50, "-"))
fr = open("document/test.txt", "r", encoding="utf-8")
print(fr.readlines(30)) # 读取30个字符所在的行
fr.close()