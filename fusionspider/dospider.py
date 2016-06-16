#-.- coding:utf-8 -.-


import json
import sys
import getopt

import cdnspider
from utils import taobao_ip

cdn={
        "wangsu":"网宿",
         "baishanyun":"白山云",
         "dilian":"帝联",
         "kuaiwang":"快网",
         "tencent":"腾讯"
    }

platform={
        "vod":"点播平台",
        "large":"大文件下载平台",
        "dd":"下载平台[新]",
        "dl":"下载平台[旧]",
        "tiny":"小文件(网页)平台",
        "ot":"小文件(网页)平台",
        "dn":"小文件(网页)平台",
        "qiniucdn":"小文件(网页)平台",
    }

def usage():
    print "Usage:fip -i [ip] ..."
    print "查询使用方式: -h"
    print "查询IP归属地: -i [ip]"
    print "查询IP归属CDN服务商: -c [ip]"
    print "查询CNAME区域覆盖: -m [cname] [isp] [provice]"


def __getplatform(string):
    platf=[]
    for st,pl in platform.items():
        for cname in string:
            if st in cname:
                platf.append(pl)
        return platf
    return "Unknow Platform"

def getRegionByDomian(domain):

    op = cdnspider.SpiderMan()

def checkcdnip(ip,isdetail=False):

    op = cdnspider.SpiderMan()

    rs = op.checkip(ip)
    s = json.loads(rs[2].encode("utf8"))

    LineCname = s["LineCname"]
    lines = ""
    for i in LineCname:
        lines += i + ","
    lines = lines[0:-1]


    cdninfo = cdn[s["cdninfo"]]
    region = taobao_ip.checkip(ip)
    print "检测IP:\t" + str(ip)
    print "========================================="
    print "线路归属:\t" + str(lines)
    print "CDN服务商:\t" + str(cdninfo)
    print "地域归属:\t" + region

def checkip(ip):

    print taobao_ip.checkip(ip)

