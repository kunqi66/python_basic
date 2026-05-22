l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
year=int(input("请输入年份:"))
month=int(input("请输入月份："))
if year%4==0 and year%100!=0 or year%400==0:
    l[2]=29
print(l[month])
