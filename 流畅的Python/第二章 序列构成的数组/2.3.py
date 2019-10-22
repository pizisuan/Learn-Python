"""
元组不仅仅是不可变的列表
"""

# 元组和记录
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(traveler_ids):
    print('%s/%s' %passport)

for country, _ in traveler_ids:
    print(country)


# 元组拆包
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates    # 元组拆包

# 应用：不使用中间变量交换两个变量的值
b, a = a, b    #

# 应用：用 * 运算符把一个可迭代对象拆开作为函数的参数
t = (20, 8)
quotient, remainder = divmod(*t)

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

# 应用：用 * 来处理剩下的元素
"""
>>> a, b, *rest = range(5)
>>> a, b, rest
(0, 1, [2, 3, 4])
>>> a, b, *rest = range(3)
>>> a, b, rest
(0, 1, [2])
>>> a, b, *rest = range(2)
>>> a, b, rest
(0, 1, [])

>>> a, *body, c, d = range(5)
>>> a, body, c, d
(0, [1, 2], 3, 4)
>>> *head, b, c, d = range(5)
>>> head, b, c, d
([0, 1], 2, 3, 4)
"""

# 命名元组
from collections import namedtuple
city = namedtuple('City','name country population coordinates')
tokyo = city('Tokyo','JP','36.933',(35.689722, 139.691667))
print(tokyo.name)
print(tokyo.country)
print(tokyo.population)
print(tokyo.coordinates)

print(tokyo._asdict())
print(city._fields)