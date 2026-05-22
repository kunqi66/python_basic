name = "张三"
age = 18
weight = 100.5
print("name = ", name, "age = ", age, "weight = ", weight)
age = 19        #变量可以重新赋值
weight = 120.0  #变量可以重新赋值
print("name = ", name, "age = ", age, "weight = ", weight)

a, b = 1, 2 #创建多个变量
c = a + b
print("a = ", a, "b = ", b, "c = ", c)

x, y = 1, 2
print("x = ", x, "y = ", y)
x, y = y, x  # 交换x,y变量的值
print("x = ", x, "y = ", y)
num1 = 20
print((num2 := 3**2) > num1)
print(num2)
print(num2:=5+6)