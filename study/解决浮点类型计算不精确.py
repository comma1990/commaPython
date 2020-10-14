# Author ： comma
# 日期 : 2020/10/15  06:28

#解决浮点类型计算不精确的问题


print(1.1+2.2)

#引入Decimal方法
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))