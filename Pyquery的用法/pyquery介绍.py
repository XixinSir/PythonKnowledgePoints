from pyquery import PyQuery as pq
import requests

print("--------------------------2、初始化----------------------------------")
#  初始化pyquery,构建一个PyQuery对象(传入字符串、URL、文件名都可以)
html = """
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""
# 声明了一个长HTML字符串,并将其当做参数传给PyQuery类,这样就完成了初始化.
doc = pq(html)
# 将初始化的对象传入CSS选择器。这里传入li节点,就可以选择所有的li节点
print(doc("li"))



print("---------初始化的参数不仅可以以字符串的形式传递,还可以传入网页的URL，只需要指定参数为url即可----------")
# PyQuery对象会首先请求这个URL,然后用得到的HTML内容完成初始化,这样就相当于用网页的源代码以字符窜的形式传递给PyQuery来初始化类
# doc = pq(url= "http://cuiqingcai.com")
doc = pq(requests.get('http://cuiqingcai.com').text)
#  print(type(doc))  # <class 'pyquery.pyquery.PyQuery'>
print(doc("title"))  # 两个是一样的
#  print(type(doc("title")))  # <class 'pyquery.pyquery.PyQuery'>


print("py里面也可以传入文件名")
'''
当然，这里需要有一个本地HTML文件demo.html，其内容是待解析的HTML字符串。
这样它会首先读取本地的文件内容，然后用文件内容以字符串的形式传递给PyQuery类来初始化。
以上3种初始化方式均可，当然最常用的初始化方式还是以字符串形式传递。
'''
# doc = pq(filename="demo.html")
# print(doc("li"))


