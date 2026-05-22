year,month,day=0,0,0
while True:
    year,month,day=map(int,input().split(' '))
    max_day=31
    if year<=0:
        print('请输入大于0的年份')
        continue
    if month<=0 or month>=12:
        print('是输入一到十二的月份')
        continue
    if month in [1,3,5,7,8,10,12]:
        max_day=31
    elif month in [2,4,6,9,11]:
        max_day=30
    else:
        if year%4==0 and year%100!=0 or year%400==0:
            max_day=29
        else:
            max_day=28
    if day<=0 or day>max_day:
        print('请输入正确的日期')
        continue
    ans=0
    for i in range(1,month):
        if month in [1,3,5,7,8,10,12]:
            ans+=31
        elif month in [4,6,9,11]:
            ans+=30
        else:
            if year%4==0 and year%100!=0 or year%400==0:
                ans+=29
            else:
                ans+=28
    ans+=day
    print(ans)
    break