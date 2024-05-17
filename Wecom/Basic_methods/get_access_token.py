# #!/usr/bin/python3
# # import numpy as np
# # import urllib.request
# # from bs4 import BeautifulSoup
# # import re
# import logging
# import sys
# import requests
# from Wecom.etc import config
#
#
# # 获取【access_token】
# #
# # 通过“客户联系的Secret获取access_token”
#
# # 配置日志记录器的根日志级别和输出地点
# logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
#
# def get_access_token():
#     url_access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
#     corpid = config.corpid
#     #secret是客户联系的密钥，注意来源
#     corpsecret = config.corpsecret
#
#     params_access_token = {
#         "corpid": corpid,
#         "corpsecret": corpsecret
#     }
#
#     # 记录即将发送的请求
#     logging.info(f'Sending request to {url_access_token} with params {params_access_token}')
#
#     response = requests.get(url_access_token, params=params_access_token)
#
#     # 记录收到的响应
#     logging.info(f'Received response: {response.status_code}, {response.text}')
#
#     data = response.json()
#     print("接口返回的data内容为：",data)
#     access_token = data.get('access_token',[])
#     print("access_token为：",access_token)
#
#     return access_token


import logging
import sys
import requests
from NewSpiderTest.Wecom.etc import config

# 配置日志记录器的根日志级别和输出地点
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def get_access_token():
    url_access_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
    corpid = config.corpid
    # secret是客户联系的密钥，注意来源
    corpsecret = config.corpsecret

    params_access_token = {
        "corpid": corpid,
        "corpsecret": corpsecret
    }

    # 记录即将发送的请求
    logging.info(f'Sending request to {url_access_token} with params {params_access_token}')

    response = requests.get(url_access_token, params=params_access_token)

    # 记录收到的响应
    logging.info(f'Received response: {response.status_code}, {response.text}')

    data = response.json()
    logging.debug("接口返回的data内容为：%s", data)

    access_token = data.get('access_token', [])
    logging.debug("access_token为：%s", access_token)

    return access_token


get_access_token()



