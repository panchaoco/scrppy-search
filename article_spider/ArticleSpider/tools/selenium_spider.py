# -*- coding: utf-8 -*-
__author__ = 'panchao'

from selenium import webdriver
from scrapy.selector import Selector

browser = webdriver.Chrome(executable_path="D:/user/chrome/chromedriver_win32/chromedriver.exe")

browser.get("https://www.zhihu.com/signin")

browser.find_element_by_css_selector(".SignFlow input[name='username']").send_keys("15520870525")
browser.find_element_by_css_selector(".SignFlow input[name='password']").send_keys("pc19950525")
browser.find_element_by_css_selector(".SignFlow button.Button.SignFlow-submitButton").click()

# t_selector = Selector(text=browser.page_source)
#
# print(t_selector.css('.tm-price-panel .tm-price::text').extract())
#
# browser.quit()