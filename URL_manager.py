#!/usr/bin/python3
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import re


class UrlManger(object):

    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()


    # 向管理器添加URL
    def add_new_url(self,url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 向管理器批量添加URL
    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断管理器中是否有新的待爬取的URL
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 管理器中获取新的待爬取的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

