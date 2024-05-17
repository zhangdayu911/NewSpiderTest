#!/usr/bin/python3
# import numpy as np
# import urllib.request
# from bs4 import BeautifulSoup
# import re
import requests
from NewSpiderTest.Wecom.Basic_methods.get_access_token import get_access_token


# 根据员工id的list，批量获取其客户信息
def external_contact_list():

    # 引用access_token
    access_token = get_access_token()

    # 设置初始的翻页数量cursor为空字符串，limit为每次请求的数量
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/batch/get_by_user"
    cursor = ""
    limit = 100

    # 设置初始的查询对象
    userid_list = ["333735"]

    while True:
        # 构建请求参数
        params = {
            "access_token": access_token
        }

        # 构建请求json内容
        data = {
            "userid_list": userid_list,
            "cursor": cursor,
            "limit": limit
        }

        # 发送POST请求
        response = requests.post(url, params=params, json=data)
        # 获取响应数据
        result = response.json()
        print("接口返回结果为：",result)
        external_contact_list = result.get("external_contact_list", [])

        # 如果返回结果中没有数据了，说明已经获取完毕
        if len(userid_list) < limit:
            break
        # 更新cursor，准备下一次请求
        cursor = result.get("next_cursor", "")

    return external_contact_list



