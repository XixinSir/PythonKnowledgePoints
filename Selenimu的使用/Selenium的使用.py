"""
selenium是一个自动化测试工具,利用它可以驱动浏览器执行特定的动作,如点击、下拉等动作，
同时还可以获取浏览器当前呈现的页面的源代码,做到可见即可取.

"""

# 用Selenium来驱动浏览器加载网页的话,就可以直接拿到JavaScript渲染的结果,不用担心使用的是什么加密系统
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
声明浏览器对象

browser = webdriver.Chrome()
browser = webdriver.Firefox()
browser = webdriver.Edge()
browser = webdriver.PhantomJS()
browser = webdriver.Safari()
"""




# 首先会弹出一个Chrome浏览器
browser = webdriver.Chrome()
try:
    # 浏览器会跳转到百度
    browser.get("https://www.baidu.com")
    input = browser.find_element_by_id("kw")
    # 在搜索框输入百度
    input.send_keys("Python")
    # 跳转到搜索结果页
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()


