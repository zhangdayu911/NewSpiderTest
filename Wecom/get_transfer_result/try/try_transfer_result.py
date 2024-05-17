#!/usr/bin/python3
import requests
import logging
import sys
from NewSpiderTest.Wecom.Basic_methods.get_access_token import get_access_token



# 配置日志记录器的根日志级别和输出地点
logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)



def get_transfer_result():


    #“查询客户接替状态”接口内容
    url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/transfer_result?"
    access_token = get_access_token()
    handover_userid = "002663"
    takeover_list = "15806233720"
    # print(url)
    # print(access_token)



    # 构建请求参数
    params = {
    "access_token": access_token,
    }

    data = {
    "handover_userid": handover_userid,
    "takeover_userid": takeover_list
    }

    logging.info(f'发送请求 to {url} with params {params} and data {data}')

    # 发送GET请求获取客户list
    response = requests.post(url, params=params, json=data)
    # print(response)
    data = response.json()
    print(data)





get_transfer_result()