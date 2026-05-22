import keyword
print('第二题')
def calc_area(width,height,unit='cm'):
    s = width * height
    print(f'计算结果为{s}{unit}')

calc_area(3,4)

print('='*100)
print('第三题')
def print_rectangle(line,colum,sign='*'):
    if (isinstance(line, int) and isinstance(colum, int)
            and line > 0 and colum > 0):
        for i in range(colum):
            for j in range(line):
                print(sign,end='')
            print()
    else:
        print('请输入正整数的参数')
        return
print_rectangle(10,5)
print_rectangle(2.5,5.6)

print('='*10)
print('第四题')
def get_even(*nums):
    return [num for num in nums if num%2==0]
print(get_even(5,2,3,6,5,8,4,9,5,4))

print('='*100)
print('第五题')
def statistic(*nums):
    return sum(nums),len(nums),sum(nums)/len(nums)
print(statistic(1,2,3,4,5))

print('='*100)
print('第六题')
def build_str(prefix,suffix,seq,*parts):
    return prefix + seq.join(parts) + suffix

def fun_a(*name,**note_book):
    print(note_book)

fun_a(5,6,a = 56,张三 = '666')

