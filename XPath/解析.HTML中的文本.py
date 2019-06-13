# 导入lxml库的etree模块
from lxml import etree
# XPath对网页的解析过程

html = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html)
print(result.decode("utf-8"))

# 所有节点:    一般用//开头的XPath规则来选取所有符合要求的节点.
print("------------//所有节点----------------")
html = etree.parse("./test.html",etree.HTMLParser())
# *代表匹配所有节点,就是整个HTML文本中的所有节点都会被获取。
# 结果返回一个列表,每个元素都是Element类型,后面跟了节点的名称,如html等,所有节点都包含在列表中了
result = html.xpath("//*")
print(result)

print("------------------获取指指定节点,这里是li节点-------------------")
html = etree.parse("./test.html",etree.HTMLParser())
result = html.xpath("//li")
print(result)


print("------------------------获取子节点  /直接子节点   //子孙节点------")
html = etree.parse("./test.html",etree.HTMLParser())
# 所有li节点的所有直接a子节点
result = html.xpath("//li/a")
print(result)

# 获取ul节点下的所有子孙a节点
html = etree.parse("./test.html",etree.HTMLParser())
result = html.xpath("//ul//a")
# result = html.xpath("//ul/a")  # []
print(result)


print("------------------------父节点---------------------------------")
# 首先选中href属性为link4.html的a节点,然后再获取其父节点后,然后再获取class属性
result = html.xpath('//a[@href="link4.html"]/../@class')  # 目标li节点的class
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)

print("--------------------------用@符号进行属性顾虑----------------------------")
# 选取class为item-0的li节点
html = etree.parse("./test.html",etree.HTMLParser())
result = html.xpath("//li[@class='item-0']")
print(result)


print("-----------------------------文本获取-----------------------------------")
# 用XPath中的text()方法获取节点中的文本
'''
奇怪的是，我们并没有获取到任何文本，只获取到了一个换行符，这是为什么呢？
因为XPath中text()前面是/，而此处/的含义是选取直接子节点，
很明显li的直接子节点都是a节点，文本都是在a节点内部的，
所以这里匹配到的结果就是被修正的li节点内部的换行符，因为自动修正的li节点的尾标签换行了。

其中一个节点因为自动修正，li节点的尾标签添加的时候换行了，
所以提取文本得到的唯一结果就是li节点的尾标签和a节点的尾标签之间的换行符。

'''
result = html.xpath("//li[@class='item-0']/text()")  # ['\n     ']
print(result)

"""
可以看到，这里的返回值是两个，内容都是属性为item-0的li节点的文本，
这也印证了前面属性匹配的结果是正确的。

这里我们是逐层选取的，先选取了li节点，又利用/选取了其直接子节点a，
然后再选取其文本，得到的结果恰好是符合我们预期的两个结果。
"""
result = html.xpath('//li[@class="item-0"]/a/text()')
print(result)  # ['first item', 'fifth item']



"""
不出所料，这里的返回结果是3个。可想而知，这里是选取所有子孙节点的文本，
其中前两个就是li的子节点a节点内部的文本，另外一个就是最后一个li节点内部的文本，即换行符。

所以说，如果要想获取子孙节点内部的所有文本，可以直接用//加text()的方式，
这样可以保证获取到最全面的文本信息，但是可能会夹杂一些换行符等特殊字符。
如果想获取某些特定子孙节点下的所有文本，可以先选取到特定的子孙节点，
然后再调用text()方法获取其内部文本，这样可以保证获取的结果是整洁的。
"""
result = html.xpath('//li[@class="item-0"]//text()')  # ['first item', 'fifth item', '\n     ']
print(result)

print("------------------------------属性获取@----------------------------------")
"""
这里我们通过@href即可获取节点的href属性。注意，此处和属性匹配的方法不同，
属性匹配是中括号加属性名和值来限定某个属性，如[@href="link1.html"]，
而此处的@href指的是获取节点的某个属性，二者需要做好区分。
"""
result = html.xpath("//li/a/@href")
print(result)


print("------------------------------属性多值匹配---------------------------------------")
text1 = """
<li class="li li-first"><a href="link.html">first item</a></li>
"""
html1 = etree.HTML(text1)
# HTML文本中的li节点的class属性有两个值li和li-first  若用之前的属性匹配获取,就无法匹配了
result1 = html1.xpath("//li[@class ='li']/a/text()")  # []
print(result1)

print("-------------属性有两个值,就要用到contains()函数-------------")
result2 = html1.xpath("//li[contains(@class,'li')]/a/text()")
print(result2)
print("此种方式在某个节点的某个属性有多个值时经常用到,如某个节点的class属性通常有多个")



print("-------------------------多属性匹配--------------------------------")
text2 = """
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
"""
html2 = etree.HTML(text2)

"""
这里的li节点又增加了一个属性name。要确定这个节点，需要同时根据class和name属性来选择，
一个条件是class属性里面包含li字符串，另一个条件是name属性为item字符串，二者需要同时满足，
需要用and操作符相连，相连之后置于中括号内进行条件筛选。
"""

# https://cuiqingcai.com/5545.html
result2 = html2.xpath("//li[contains(@class,'li') and @ name = 'item']/a/text()")
print(result2)

print("----------------------按序选择-----------------------")
text = """
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
"""


html = etree.HTML(text)
result = html.xpath("//li[1]/a/text()")  # ['first item']
print(result)
result = html.xpath('//li[last()]/a/text()')  # ['fifth item']
print(result)
result = html.xpath("//li[position()<3]/a/text()")  # ['first item', 'second item']
print(result)
result = html.xpath("//li[last()-2]/a/text()")  # ['third item']
print(result)
"""
第一次选择时,选取第一个li节点,中括号传入数字1即可.以1开头,和代码中的不同
第二次选择时,是最后一个li节点,中括号传入last()即可,返回的便是最后一个li节点
第三次选择时,选择了位置小于3的li节点,也就是位置序号为1和2的节点,结果就是前两个li节点
第四次选择时,选择了倒数第三个li节点,中括号中传入last()-2即可.因为last()是最后一个,所以last()-2是倒数第三个
"""

print("---------------------------------节点轴选择--------------------------------")
print("XPath提供了很多节点轴选择方法,包括获取子元素、兄弟元素、父元素、祖先元素")
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
result = html.xpath('//li[1]/attribute::*')
print(result)
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
result = html.xpath('//li[1]/descendant::span')
print(result)
result = html.xpath('//li[1]/following::*[2]')
print(result)
print("第一次选择时,调用了ancestor轴,可以获取所有祖先节点.其后需要跟两个冒号,然后是节点的选择器,这里直接使用*,表示匹配所有节点,因此返回结果是第一个li节点的所有祖先节点,包括html、body、div和ul")
































