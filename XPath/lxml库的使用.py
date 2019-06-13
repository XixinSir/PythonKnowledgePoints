# 导入lxml库的etree模块
from lxml import etree
'''
使用之前,首先要确保安装好lxml库.
下面为使用XPath对网页进行解析的过程
'''
# 声明一段HTML文本
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

# 调用HTNL类进行初始化,构造一个XPath解析对象
html = etree.HTML(text)
# HTML文本中最后一个li节点是没有闭合的,但是etree模块可以自动修正HTML文本
# 调用tostring()方法即可输出修正后的HTML代码,但是结果是bytes类型。调用decode()方法将其转成str类型
result = etree.tostring(html)
print(type(result))
print(result.decode("utf-8"))
# 经过上步的处理之后,li节点标签被补全,并且还自动添加了body、html节点。
