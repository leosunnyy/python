#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : html_downloader.py
# @Author: leosunnyy
# @Email: leosunnyy@gmail.com
# @Date  : 2017/11/1
# @Desc  :
import urllib2


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        return response.read()
