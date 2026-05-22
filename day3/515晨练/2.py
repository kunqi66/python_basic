import decimal
high = decimal.Decimal(input('请输入身高'))
weight = decimal.Decimal(input('请输入体重'))
bmi = weight/(high**2)
print(f'身高：{high}米，体重：{weight}kg，你的BMI为{round(bmi,2)}')