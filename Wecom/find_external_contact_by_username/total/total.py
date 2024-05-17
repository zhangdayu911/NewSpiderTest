#!/usr/bin/python3
# import numpy as np
# import urllib.request
# from bs4 import BeautifulSoup
# import re
import requests



# 获取【access_token】
#
# 通过“客户联系的Secret获取access_token”
url_access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
corpid = "ww2e4c6332297dc5a3"
corpsecret = "WmS9ZuBnZMLpiH911OiiDGkEjD0myJIpE6_aU78GAcs"

params_access_token = {
    "corpid": corpid,
    "corpsecret": corpsecret
}

response = requests.get(url_access_token, params=params_access_token)
data = response.json()
print("接口返回的data内容为：",data)

access_token = data.get('access_token',[])
print("access_token为：",access_token)



# 获取【客户列表】
#
#
url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/list?"
userid = "333735"

# 构建请求参数
params = {
    "access_token": access_token,
    "userid": userid
}

# 发送GET请求获取客户list
response = requests.get(url, params=params)
data = response.json()
external_userid = data.get('external_userid',[])
print("external_userid为如下list：",external_userid)

count = len(external_userid)
print("external_userid的数量为：",count)



# 获取【客户详情】
#
#
url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/batch/get_by_user"

# 设置初始的cursor为空字符串，limit为每次请求的数量
cursor = ""
limit = 100
userid_list = [userid]

while True:
    # 构建请求参数
    params = {
        "access_token": access_token
    }

    # 构建请求体
    data = {
        "userid_list": userid_list,
        "cursor": cursor,
        "limit": limit
    }

    # 发送POST请求
    response = requests.post(url, params=params, json=data)

    # 获取响应数据
    result = response.json()
    # print("接口返回结果为：",result)

    # 处理获取的数据，这里假设获取到的数据在result["external_userid_list"]
    external_contact_list = result.get("external_contact_list",[])
    print("解析json中的external_contact_list为：",external_contact_list)

    user_name = "当当"

    for i in external_contact_list:
        external_contact = i["external_contact"]
        if external_contact['name']==user_name:
            print("解析",user_name,"的相关信息为:",external_contact)
            print("解析",user_name,"的unionID信息为:",external_contact["unionid"])
            break


    # 如果返回结果中没有数据了，说明已经获取完毕
    if len(userid_list) < limit:
        break

    # 更新cursor，准备下一次请求
    cursor = result.get("next_cursor", "")

# 处理完所有数据
print("finish")


