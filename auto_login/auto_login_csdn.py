#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : aoto_login_csdn.py
# @Author: leosunnyy
# @Email: leosunnyy@gmail.com
# @Date  : 2017/11/3
# @Desc  :

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os
#firefoxdriver = "C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
#os.environ["webdriver.firefox.driver"] = firefoxdriver
#driver = webdriver.Firefox(executable_path = 'C:\Program Files (x86)\Mozilla Firefox')
driver = webdriver.Firefox()
driver.get("https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn")
elem_user = driver.find_element_by_name("username")
elem_user.send_keys("your user name")
elem_pwd = driver.find_element_by_name("password")
elem_pwd.send_keys("your password")
elem_pwd.send_keys(Keys.RETURN)
#time.sleep(5)
assert "baidu" in driver.title
driver.close()
driver.quit()
