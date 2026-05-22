n1_sum=0
n2_sum=0
while 1:
    a=int(input())
    if a>0:
        n1_sum+=1
    elif a<0:
        n2_sum+=1
    else:
        break
print(f'正数的个数为{n1_sum}')
print(f'负数的个数为{n2_sum}')