n=int(input('输入自然数：'))
def gcd_subtraction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
print(int(2*n/gcd_subtraction(2,n)))

if n%2 == 0:
    print(n)
else:
    print(n<<1)

print(n<<(n&1))