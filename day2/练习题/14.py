while True:
    year,month,day=map(int,input().split(' '))
    l=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    ans=0
    if year%4==0 and year%100!=0 or year%400==0:
        l[2]=29
    if year<=0:
        print('请输入大于0的年份')
        continue
    if month<=0 or month>=12:
        print('是输入一到十二的月份')
        continue
    if day<=0 or day>=l[month]:
        print('请输入正确的日期：')
        continue
    for i in range(1,month):
        ans+=l[i]
    ans+=day
    print(ans)
    break
