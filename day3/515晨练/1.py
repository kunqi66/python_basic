import decimal
h_te = decimal.Decimal(input())
s_te = (h_te-32)/decimal.Decimal('1.8')
print(f'摄氏温度为{round(s_te,2)}\n华氏温度为{round(h_te,2)}')
