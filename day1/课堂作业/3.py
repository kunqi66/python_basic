import decimal
from itertools import count

unit_price=decimal.Decimal('5.235')
count_num=6
print(round(count_num*unit_price,2))