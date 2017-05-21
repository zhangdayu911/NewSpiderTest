#!/usr/bin/python3
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import re

class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
        pass


    def output_html(self):
        #'w'为写模式，write
        fout = open('output.html','w',encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        # fout.write('<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">')



        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td>%s</td>' % data['url'])
            fout.write('<td>%s</td>' % data['title'])
            fout.write('<td>%s</td>' % data['summary'])
            fout.write('</tr>')


        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        pass
