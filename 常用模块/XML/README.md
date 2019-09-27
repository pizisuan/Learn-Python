# XML 相关模块

## XML 简介 
> XML（可扩展性标记语言 Extensible Markup Language）是一种非常常用的文件类型，被设计用来传输和存储数据而不是显示数据（HTML用于显示数据）。

## XML 格式
主要包括以下三个方面：
1. 标签/元素 --- breakfast_menu, food, name, price, description, calories 
2. 属性 --- food 标签中的 time, cooker
3. 数据 --- 标签中的具体内容


```xml
<?xml version="1.0" encoding="UTF-8"?>
<breakfast_menu>
    <food time='20190927' cooker='Pizisuan'>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>
            Two of our famous Belgian Waffles with plenty of real maple syrup
        </description>
        <calories>650</calories>
    </food>
    <food time='20190303' cooker='A Li'>
        <name>Strawberry Belgian Waffles</name>
        <price>$7.95</price>
        <description>
            Light Belgian waffles covered with strawberries and whipped cream
        </description>
        <calories>900</calories>
    </food>
</breakfast_menu>
```

## XML 读取操作
有以下两种方式可以对XML字符串进行操作：
1. 通过字符串方式读取，参数为XML字符串，直接返回的是一个根Element对象
2. 从XML文件中读取，用*getroot*函数获取根Element对象

```python
from xml.etree import ElementTree

# 方式一: 通过字符串方式读取
xml_str = """<?xml version="1.0" encoding="UTF-8"?>
    <breakfast_menu>
        <food time='20190927' cooker='Pizisuan'>
            <name>Belgian Waffles</name>
            <price>$5.95</price>
            <description>
                Two of our famous Belgian Waffles with plenty of real maple syrup
            </description>
            <calories>650</calories>
        </food>
        <food time='20190303' cooker='A Li'>
            <name>Strawberry Belgian Waffles</name>
            <price>$7.95</price>
            <description>
                Light Belgian waffles covered with strawberries and whipped cream
            </description>
            <calories>900</calories>
        </food>
    </breakfast_menu>
"""
root = ElementTree.fromstring(xml_str)

# 方式二：通过xml文件方式读取
tree = ElementTree.parse("test.xml")
root = tree.getroot()
```

## 访问XML元素：标签（tag）、属性（attrib）、值（text）
主要包括以下方面内容：
1. 访问Element元素对象的标签、属性、值
```python
tag = element.tag
attrib = element.attrib
value = element.text
```
2. 访问子节点元素对象及其标签、属性、值
```python
for son in root:
    print(son,son.tag,son.attrib,son.text)
    for grandson in son:
        print(grandson, grandson.tag, grandson.attrib, grandson.text)
```
3. Elements元素对象都是可迭代的对象，可以直接对其list(Element)将其转化为列表，其列表元素为当前Elements元素的子节点列表
```python
root = ElementTree.fromstring(xml_str)
print(list(root))
```
4. 按照元素名字访问或者迭代元素

   * Element.iter("tag")
   > 获取该节点所包含的所有标签为"tag"的节点（**子孙节点**）。
   
   * Element.findall("tag")
   > 获取**当前节点**中标签为"tag"的**所有直接子节点**，返回结果是一个可迭代对象。
   
   * Element.find("tag")
   > 获取标签为"tag"的**第一个直接子节点**，如没有，返回None 。

```python
root = ElementTree.fromstring(xml_str)

# 返回一个可迭代对象，迭代这个对象可以迭代出包括根节点在内的所有节点（所有子、孙节点）
print(root.iter()) 

# 返回一个可迭代对象，迭代这个对象（root）可以迭代出标签名为"name"的所有节点（子、孙节点）
print(root.iter("name"))

# 返回一个列表，列表元素为当前节点（root）的标签名为"food"的所有子节点
print(root.findall("food"))

# 返回一个节点，该节点市当前节点（root）中第一个标签名为"food"的子节点
print(root.find("food"))

```
