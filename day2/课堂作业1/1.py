# 练习1
a=int(input("请输入一个整数："))
b=int(input("请输入另一个整数："))
print("两个整数的和是：",a+b)
print("两个整数的差是：",a-b)
print("两个整数的积是：",a*b)
print("两个整数的商是：",a/b)

# 练习2
r=float(input("请输入一个半径："))
c=2*3.14*r
print("圆的周长是：",c)
s=3.14*r**2
print("圆的面积是：",s)

#练习3
a=int(input("请输入一个三位数整数："))
print("这个三位数的个位数是：",a%10)
print("这个三位数的十位数是：",a//10%10)
print("这个三位数的百位数是：",a//100)

# 练习4
a=int(input("请输入一个数："))
if a%2==0 and a%3==0:
    print("这个数是偶数和3整除")
else:
    print("这个数不是偶数和3整除")

# 练习5
a=int(input("请输入一个整数："))
if a%3==0 or a%5==0 or a%7==0:
    print("这个数是3或5或7的倍数")
else:
    print("这个数不是3或5或7的倍数")

# 练习6
a=int(input("请输入一个整数："))
b=a//24
if a%24!=0:
    b+=1
print("这个任务需要：{b}天".format(b=b))



