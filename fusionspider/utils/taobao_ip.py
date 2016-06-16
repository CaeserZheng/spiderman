#-.- coding:utf-8 -.-
__author__ = 'caeser'

import requests
import json

'''
淘宝IP库
'''
def checkip(ip):
    api = "http://ip.taobao.com/service/getIpInfo.php?ip="
    url = api + str(ip)

    rs = requests.get(url)
    rs = rs.json()
    code = rs["code"]
    data = rs["data"]
    value = ""
    if code == 0:
        value = "Country: " +data["country"] + "\t" \
                "Area: " + data["area"] + "\t" \
                "Region: " + data["region"] + "\t" \
                "City: " + data["city"] + "\t" \
                "isp:" + data["isp"]
        return value
    else:
        return "Code: " + str(code) +"IP归属地查询失败"





