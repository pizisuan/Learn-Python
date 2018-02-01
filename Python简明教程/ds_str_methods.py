# 这是一个字符串对象
name = 'Swaroop'
if name.startswith('Swa'):
  print('Yes, the string starts with "Swa"')
if 'a' in name:
  print('Yes, it contains the string "a"')
if name.find('war') != -1:
  print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


# 输出
# Yes, the string starts with "Swa"
# Yes, it contains the string "a"
# Yes, it contains the string "war"
# Brazil_*_Russia_*_India_*_China
