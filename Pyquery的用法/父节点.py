from pyquery import PyQuery as pq

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''


"""
这里我们首先用.list选取class为list的节点，
然后调用parent()方法得到其父节点，其类型依然是PyQuery类型。

这里的父节点是该节点的直接父节点,它不会再去查找父节点的父节点,即祖先节点
"""

# 构建一个pyquery对象
doc = pq(html)
# 选取class为list的节点
items = doc(".list")
print("调用parent()方法得到父节点,类型依然是pyquery类型    直接父节点")
container = items.parent()
print(type(container))
print(container)

print("------------------------parents()用于获取祖先节点-------------------")

"""
结果有两个:一个是class为wrap的节点，
一个是id为container的节点。也就是说，
parents()方法会返回所有的祖先节点。 包括他的直接父节点
"""
doc = pq(html)
items = doc(".list")
container = items.parents()
print(container)

"""
如果想要筛选某个祖先节点,可以向parents()方法传入CSS选择器,就会返回祖先节点中符合CSS选择器的节点
"""
parent = items.parents(".wrap")
print(parent)