"""
本模块用于解析xml

@author: Pizisuan
@date: 2019/09/27
@function: parse_xml
"""

from xml.etree import ElementTree

def parse_xml(xml_str):
    """
    解析xml字符串
    :param xml_str: 输入xml字符串
    :return:
    """
    try:
        root = ElementTree.fromstring(xml_str)
    except:
        print("无法解析,请检查xml字符串格式")
    else:
        for son in root:
            print("---------------")
            print("当前节点是{}的子节点{}".format(root.tag, son.tag))
            print("属性及内容分别为：", son.attrib, son.text)
            for grandson in son:
                print("当前节点是{}的子节点{}".format(son.tag, grandson.tag))
                print("属性及内容分别为：", grandson.attrib, grandson.text)
        print("done")



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

if __name__ == "__main__":
    parse_xml(xml_str)
