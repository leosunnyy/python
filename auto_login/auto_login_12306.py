#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 12306_3.py.py
# @Author: leosunnyy
# @Email: leosunnyy@gmail.com
# @Date  : 2017/11/8
# @Desc  :
import cookielib
import ssl
import urllib
import urllib2
import json
import login_info

# 关闭ssl证书验证
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
# 加载和保存cookie
c = cookielib.LWPCookieJar()
# 处理HTTP cookie
cookie = urllib2.HTTPCookieProcessor(c)
# 生成一个opener，并通过该opener来访问URL;
opener = urllib2.build_opener(cookie)

req = urllib2.Request(
    'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.18261509176744273')
# req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36)')
# 在请求中加入cookie
codeimg = opener.open(req).read()
with open('./code.png', 'wb') as fn:
    fn.write(codeimg)
# 输入验证码图片坐标
code = raw_input('请输入验证码图片的坐标：')
req = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check')
data = {
    'answer': code,
    'login_site': 'E',
    'rand': 'sjrand'
}

data = urllib.urlencode(data)
# req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36)')
html = opener.open(req, data=data).read()
print html
result = json.loads(html)
if result['result_code'] == '4':
    print '验证码校验成功'
elif result['result_code'] == '8':
    print '验证码校验失败,信息为空'
else:
    print '验证码校验失败'
req = urllib2.Request('https://kyfw.12306.cn/passport/web/login')

data = {
    'username': login_info.username,
    'password': login_info.password,
    'appid': 'otn'
}
data = urllib.urlencode(data)
# req.add_header('Referer', 'https://kyfw.12306.cn/otn/login/init')
# req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36)')

html = opener.open(req, data=data).read()
print html
result = json.loads(html)
if result['result_code'] == 0:
    print '登陆成功'
else:
    print '登陆失败'
