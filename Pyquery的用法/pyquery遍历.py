from pyquery import PyQuery as pq

html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>4
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

doc = pq(html)
"""
infor = doc(".wrap #container .item-0.active").items()  只返回第三个li元素
infor = doc(".wrap #container .item-0").items()  返回三个元素
infor = doc(".wrap #container .item").items() 



infor = doc(".wrap #container li").items()  返回全部的li元素
infor = doc(".wrap    li").items()  返回的和上一行的一样 而且li前面的不管是不是他的直接父节点 结果都不变  即使li前面多打几个空格也不影响
"""


infor = doc(".wrap   li").items()  # 加上items之后  infor的类型是<class 'generator'>
# print(infor)
# print(type(infor))
for item in infor:
    """
    print(item.find("a"))  没有a节点的显示为空  有的显示此节点
    print(item.text())  显示文本信息
    
    """
    print(item.attr("class"))
