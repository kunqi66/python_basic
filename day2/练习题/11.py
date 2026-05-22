for i in range(6):
    for j in range(i):
        print('*',end='')
    print('')
print('')
for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    for j in range(1,2*i):
        print('*',end='')
    print('')


for i in range(1,6):
    for j in range(1,6-i):
        print(' ',end='')
    if i==1:
        print('*')
    else:
        print('*', end='')
        for j in range(1,2*i-2):
            print(' ',end='')
        print('*')
for i in range(1,5):
    for j in range(1,i+1):
        print(' ',end='')
    if i==4:
        print('*')
    else:
        print('*',end='')
        for j in range(1,6-2*i+2):
            print(' ',end='')
        print('*')

'''
1   5  6-2i+1
2   3
3   1
4   0
'''