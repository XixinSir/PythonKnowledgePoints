from pyquery import PyQuery as pq
html = """
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
"""
# 首先初始化PyQuery对象
doc = pq(html)
# 传入一个CSS选择器 #container .list li   意思是选取节点id为container的节点,然后再选取其内部的class为list的节点内部的所有li节点.然后,打印输出。
print(doc("#container .list li"))
# 类型依然是PyQuery类型
print(type(doc("#container .list li")))

print("4、一些常用的查询函数,这些函数和jQuery中函数的用法完全相同")
# 子节点 查找子节点时,需要用到find()方法,此时传入的参数是CSS选择器
doc = pq(html)
# 选取class为list的节点
items = doc(".list")
print(type(items))
print(items)
"""
调用find()方法,传入CSS选择器,选取内部的li节点,最后打印输出.
find()方法会将符合条件的所有节点选择出来,结果的类型是PyQuery类型
find()的查找范围是所有子孙节点,如果只想查找子节点,可以用Children()方法
"""

lis = items.find("li")
print(type(lis))
print(lis)
