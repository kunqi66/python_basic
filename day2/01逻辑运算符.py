# -------------逻辑运算符---------------
print(False and True)  # False
print(False or True)  # True
print(not False)  # True
print(not True)  # True

print(5 and 8)  # 8 非0表示True，0表示False
print(0 and 8)  # 0
print(5 or 8)  # 5
print(0 or 8)  # 8
print(not 5)  # False
print(not 0)  # False

# 三目运算
a = 10
b = 9
max_num = a if a> b else b # if-else表达式
print(max_num)

# is 和 not is 用来判断是不是引用的同一个对象类似id(a)==id(b)
a = "123"
b = str(123)
print(a is b) # False，地址不同
print(id(a) == id(b)) # False，地址不同
print(a == b) #  True，内容相同