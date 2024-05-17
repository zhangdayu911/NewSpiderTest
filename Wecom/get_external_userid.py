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
def get_external_userid():
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list?"
    userid = "333735"
    access_token = get_access_token()


    # 构建请求参数
    params = {
        "access_token": access_token,
        "userid": userid
    }


    # 发送GET请求获取客户list
    response = requests.get(url, params=params)
    print(response)
    data = response.json()
    print(data)
    external_userid = data.get('external_userid', [])
    print("external_userid为如下list：", external_userid)

    count = len(external_userid)
    print("external_userid的数量为：", count)

    return external_userid



# # 测试本方法结果
# result = get_external_userid()
# print(result)


