import decimal


#type() 与 isinstance()
a=10
b=True
print("a的类型",type(a))
print("b的类型",type(b))

print(isinstance(a,object))
print(isinstance(b,bool))
print(isinstance(a,int))
print(isinstance(a,float))

#整型
a=10
print(a)
a=123_456_789
print(a)
#整数池
a = 10
b = 10
print(a == b)
print(id(a) == id(b))

a = 300
b = 300
print(a == b)
print(id(a) == id(b))

#浮点数
f=2.2131513146843515616165
print(f)  #直接使用浮点精度有限
a = 3.1415926e7 # 科学计数法表示
print(a)
a = 3.1415926e5 # 科学计数法表示
print(a)
a = 31415.926e-5 # 科学计数法表示
print(a)
a = 3.14_15_926 #使用下划线作为数字分隔符
print(a)
#Decimal
a=decimal.Decimal("0.13213516616655"
                  "556"
                  "5"
                  "5"
                  "56")
print(a)  #高精度浮点数

#布尔
a = True
b = 1
c = False
d = 0

print("布尔标记1",a == b)
print("布尔标记2",c == d)
print("布尔标记3",a + 1)

print(a is b)
print(c is d)

flag = None
if flag:
    print("None")

flag = 1.0
if flag:
    print("0.0")

flag = ""
print(bool(flag))
if flag:
    print("空字符串")

flag = []
if flag:
    print("空列表")



