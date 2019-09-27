# XML 相关模块

## XML 简介 
> XML（可扩展性标记语言eXtensible Markup Language）是一种非常常用的文件类型，被设计用来传输和存储数据而不是显示数据（HTML用于显示数据），XML 标签没有被预定义。您需要自行定义标签。

## XML 格式
主要包括以下三个方面：
1. 标签/元素 
2. 属性 
3. 数据 


```xml
<?xml version="1.0" encoding="UTF-8"?>
<breakfast_menu>
    <food>
        <name>Belgian Waffles</name>
        <price>$5.95</price>
        <description>
            Two of our famous Belgian Waffles with plenty of real maple syrup
        </description>
        <calories>650</calories>
    </food>
    <food>
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
2. 从xml文件中读取，用getroot获取根节点，根节点也是Element对象

```python
from xml.etree import ElementTree

# 方式一: 通过字符串方式读取
xml_str = """
    <?xml version="1.0" encoding="UTF-8"?>
    <breakfast_menu>
        <food>
            <name>Belgian Waffles</name>
            <price>$5.95</price>
            <description>
                Two of our famous Belgian Waffles with plenty of real maple syrup
            </description>
            <calories>650</calories>
        </food>
        <food>
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
