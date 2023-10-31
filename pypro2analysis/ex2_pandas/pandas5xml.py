# 웹문서 읽기 : XML
import xml.etree.ElementTree as etree

xmlf = open("../testdata/my.xml", mode="r", encoding="utf-8").read()
print(xmlf, type(xmlf))  # <class 'str'>
root = etree.fromstring(xmlf)
print(root, type(root))  # <class 'xml.etree.ElementTree.Element'> 파싱이 되어 Element 객체가 됨
print(root.tag, ' ', len(root))
print()
xmlfile = etree.parse("../testdata/my.xml")
print(xmlfile, type(xmlfile))  # <class 'xml.etree.ElementTree.Element'>
root = xmlfile.getroot()
print(root.tag)  # items
print(root[0].tag)  # item
print(root[0][0].tag)  # name
print(root[0][1].tag)  # tel
print(root[0][0].attrib)  # {'id': 'ks1'}
print(root[0][0].attrib.keys())
print(root[0][0].attrib.values())
print()
myname = root.find('item').find('name').text
print(myname)  # 홍길동
print()
for child in root:
    # print(child.tag)  # item 2개 잡힘
    for child2 in child:
        print(child2.tag, child2.attrib)
        
print()
children = root.findall('item')
print(children)
for it in children:
    re_id = it.find('name').get('id')  # name 안 속성 값 id를 읽음
    re_name = it.find('name').text
    re_tel = it.find('tel').text
    print(re_id, re_name, re_tel)
