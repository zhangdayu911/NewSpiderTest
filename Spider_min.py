#!/usr/bin/python3
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import re
import Html_downloader
import URL_manager
import Html_outputer
import Html_parser



class Spider_main(object):
    def __init__(self):
        self.urls = URL_manager.UrlManger()
        self.downloader = Html_downloader.HtmlDownloader()
        self.parser = Html_parser.HtmlParser()
        self.outputer = Html_outputer.HtmlOutputer()

    def craw(self,root_url):
        count = 1
        # 添加到新URL库中
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                # 输出url
                print('craw %d : %s' % (count, new_url))

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 50:
                    break
                count += 1
            except Exception as e:
                print(e)
                print("craw failed")
        #输出数据
        self.outputer.output_html()
        pass



if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = Spider_main()
    obj_spider.craw(root_url)
print("成功")