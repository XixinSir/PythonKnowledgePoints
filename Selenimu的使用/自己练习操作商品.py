import requests
from pyquery import  PyQuery as pq
from urllib.parse import quote

def get_product(url):
    """
    获取商品的信息
    :param page:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 QIHU 360EE"
    }
    # doc = pq(url= url)
    doc = pq(requests.get(url,headers= headers).text)
    items = doc(".grid g-clearfix .items .div").items()
    for item in items:
        print(item.find(""))







get_product("https://s.taobao.com/search?q=ipad&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132")
