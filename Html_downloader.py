#!/usr/bin/python3
import numpy as np
import urllib.request
from bs4 import BeautifulSoup
import re


class HtmlDownloader(object):


    def download(self, url):
        if url is None:
            return

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return
        else:
            return  response.read().decode("utf-8")