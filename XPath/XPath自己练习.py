from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
    </ul>
 </div>
'''
html = etree.HTML(text)
print(html)
print("--------------------------属性-----------------------------")
result = html.xpath("//li[@class='item-0']/a/text()")
print(result)
result = html.xpath("//li[@class='item-0']/a/text()/..")
print(result)

print("--------------------------父节点(/..)---------------------------")
result = html.xpath("//li/..//a/..")
print(result)

print("-------------------查找div------------------------")
result = html.xpath("//div")
for i in result:
    m = i.xpath(".//a[@href='link1.html']/text()")
    # m = i.xpath(".")
    print(m)
    # print(i)

# result = result.xpath("./*")

