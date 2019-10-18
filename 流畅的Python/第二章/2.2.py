"""
列表推导和生成器表达式
"""

# 列表推导同filter和map的比较
symbols = '$¢£¥€¤'
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))


# 笛卡尔乘积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]


# 生成器表达式
symbols = '$¢£¥€¤'
print(tuple(ord(symbol) for symbol in symbols))