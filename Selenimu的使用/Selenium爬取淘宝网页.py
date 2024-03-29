from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = "ipad"

def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print("正在爬取第",page,"页")
    try:
        url = 'https://www.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:

            # mainsrp-pager > div > div > div > div.form > span.btn.J_Submit
            # <span class="btn J_Submit" role="button" tabindex="0">确定</span>
            input = wait.until(EC.presence_of_element_located(By.CSS_SELECTOR,"#mainsrp-pager div.form > input"))
            submit = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,"#mainsrp-pager div.form >span.btn.J_Submit"))
            input.clear()
            input.send_keys(page)
            submit.click()
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
            get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc("#mainsrp-itemlist .itesm .item").items()
    for item in items:
        product = {
            "image": item.find(".pic .img").attr("data-src"),
            "price": item.find(".price").text(),
            "deal": item.find(".deal-cnt").text(),
            "title": item.find(".title").text(),
            "shop": item.find(".shop").text(),
            "location": item.find(".location").text()
        }
        print(product)


index_page(2)
