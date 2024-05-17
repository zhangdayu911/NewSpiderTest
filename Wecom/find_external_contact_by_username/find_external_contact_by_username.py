#!/usr/bin/python3
# import urllib.request
# from bs4 import BeautifulSoup
# import re
# import requests
from external_contact_list import external_contact_list


# 通过目标姓名获取对应openid
target_name = "当当"

external_contact_list = external_contact_list()
for i in external_contact_list:
    external_contact = i["external_contact"]
    if external_contact["name"] == target_name:
        print(target_name,"的信息是",external_contact)
        print(target_name,"的openid是",external_contact["unionid"])
        break


