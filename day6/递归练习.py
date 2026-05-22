print('第一题')
def f_fei(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return f_fei(n-2)+f_fei(n-1)
print(f_fei(10))

print('第二题')
def f_hou(day):
    if day == 10:
        return 1
    return (f_hou(day+1)+1) * 2
print(f_hou(1))

print('第三题')
def f_tu(n):
     if n == 1 or n == 2:
         return 1
     return f_tu(n-1) + f_tu(n-2)
print(f_tu(24))