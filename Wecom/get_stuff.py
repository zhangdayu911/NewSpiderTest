#!/usr/bin/python3
# import numpy as np
# import urllib.request
# from bs4 import BeautifulSoup
# import re
import requests
from NewSpiderTest.Wecom.Basic_methods.get_access_token import get_access_token


# 获取某个员工的【客户id列表】
#
#
def get_stuff_info():
    url = "https://qyapi.weixin.qq.com/cgi-bin/user/list?"
    access_token = get_access_token()
    bumenid = "1387"

    print(url)
    print(access_token)
    print(bumenid)


    # 构建请求参数
    params = {
        "access_token": access_token,
        "department_id": bumenid
    }


    # 发送GET请求获取客户list
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    print(data)

get_stuff_info()


# # 测试本方法结果
# result = get_external_userid()
# print(result)


