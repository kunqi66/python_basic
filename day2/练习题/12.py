ans=[1]
for num in range(1,1000):
    l=[]
    num_sum = 0
    for i in range(1,num):
        if num%i==0:
            l.append(i)
    for i in l:
        num_sum+=i
    if num_sum==num:
        ans.append(num)

for i in ans:
    print(i,end=' ')
