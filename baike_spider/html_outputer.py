#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : html_outputer.py
# @Author: leosunnyy
# @Email: leosunnyy@gmail.com
# @Date  : 2017/11/1
# @Desc  :
import codecs


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = codecs.open('output.html', 'w')
        fout.write("<html>")
        fout.write("<boddy>")
        fout.write("<table>")
        fout.write("<meta charset='utf-8'>")
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</boddy>")
        fout.write("</html>")
