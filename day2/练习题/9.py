import random

right_ans=random.randint(1,100)
left = 1
right = 100
while 1:
    ans = int(input())
    if ans == right_ans:
        print('你猜对了')
        break
    elif ans > right_ans:
        print(f'你猜大了,范围在{left}~{ans}')
        right = ans
        continue
    else:
        print(f'你猜小了，范围在{ans}~{right}')
        left = ans
        continue
