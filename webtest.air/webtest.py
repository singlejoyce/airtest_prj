# -*- encoding=utf8 -*-
__author__ = "build"

from airtest.core.api import *

auto_setup(__file__)

from selenium import webdriver
from airtest.utils.selenium_proxy import WebChrome
options = webdriver.chrome.options.Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = WebChrome(chrome_options=options)
driver.implicitly_wait(20)
driver.get("http://passport.ddianle.com/register.html")
driver.find_element_by_xpath("//span[@class='unselect']").click()
driver.find_element_by_id("username").click()
driver.find_element_by_id("username").send_keys("aaaaaa")
# driver.find_element_by_id("pwd1").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[5]/div[2]/table/tbody/tr/td[2]/div/span").assert_text("请输入正确的用户名")



