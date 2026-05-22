# ------------普通输出--------------
print("hello world") # 输出单个值

a = 1
b = 2
print("a = ", a, "，b = ", b) # 输出多个参数值，用逗号分隔

#  可以指定参数的分隔符和结尾符
print("hello", "world", "python", sep="-", end=".")

# 格式化输出
print("a = %d, b = %d" % (a, b))
# -----------------%占位符-----------------
a = 1
b = 2.5
print("a = %d, b = %f" % (a, b))
# -----------------字符串.format()-----------------
x = 1
y = 2
# 方式1：不设置指定位置，按默认顺序
print("x = {}, y = {}".format(x, y))

# 方式2：设置指定位置
print("如果想要得到 x = {1}, y = {0},就需要将x = {0}, y = {1}变量的值交换".format(x, y))

# 方式3：设置指定名称
num = 10
flag = True
print("整数：{intValue}, 布尔：{boolValue}".format(intValue=num, boolValue=flag))
# -----------------f字符串-----------------
name = "Irene"
age = 18
print(f"我的名字是{name}, 我的年龄是{age}")
print(f"我的个人信息：{name=}, {age=}")
# -----------------嵌套{{}}转义-----------------
pi = 3.14
print(f"圆周率{{pi}},{pi=}")
"""
    说明： f"字符串" 与 字符串.format() 是类似的
    （1）不加格式控制
        f"文本{变量1}文本{变量2}"
        "文本{}文本{}".format(变量1,变量2)
        "文本{位置编号}文本{位置编号}".format(变量1,变量2)
        "文本{变量别名1}文本{变量别名2}".format(变量别名1=变量1,变量别名2=变量2)
    （2）加格式控制
        f"文本{变量1:格式控制}文本{变量2:格式控制}"
        "文本{:格式控制}文本{:格式控制}".format(变量1,变量2)
        "文本{位置编号:格式控制}文本{位置编号:格式控制}".format(变量1,变量2)
        "文本{变量别名1:格式控制}文本{变量别名2:格式控制}".format(变量别名1=变量1,变量别名2=变量2)
"""
name = "柴林燕"
age = 18
weight = 40.5
marry = True
#====================不加格式控制====================
print(f"姓名：{name}，年龄：{age}，体重：{weight}，婚否：{marry}")
print("姓名：{n}，年龄：{a}，体重：{w}，婚否：{m}".format(n=name,a=age,w=weight,m=marry))
print("姓名：{}，年龄：{}，体重：{}，婚否：{}".format(name,age,weight,marry))
print("姓名：{0}，年龄：{1}，体重：{2}，婚否：{3}".format(name,age,weight,marry))

#====================加格式控制====================
print("姓名：{:<10s}年龄：{:<10d}体重：{:<10.2f}".format(name,age,weight))
print("姓名：{0:<10s}年龄：{1:<10d}体重：{2:<10.2f}".format(name,age,weight))
print(f"姓名：{name:<10s}年龄：{age:<10d}体重：{weight:<10.2f}")