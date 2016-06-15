#-.- coding:utf-8 -.-

from qiniu import Auth
import http
import requests
import json
'''
spiderman服务
ip查询

'''

Host="api.qiniu.com"

access_key="kIqyOV6XBtP5NvvXmoWHdp0uRxkdtRTlQcpQOmD1"
screen_key="LvkTLk_dy8RxJDE_bPi4VZ-SNI_BdoLklvXeowo0"

class SpiderMan():
    def __init__(self):

        if not (access_key or screen_key ):
            raise ValueError("invalid access_key or screen_key!!")

        self.op = Auth(access_key,screen_key)


    def register(self,cname,POST=False,DELETE=False):
        url = "http://" + Host + "/v1/cname/" + cname
        token = self.op.token_of_request(url)
        token="QBox " + token
        header={'Authorization':str(token)}

        if POST:
            re = requests.post(url,headers=header)
            return re.status_code,re.headers,re.text

        elif DELETE:
            re = requests.delete(url,headers=header)
            return re.status_code,re.headers,re.text
        else:
            raise ValueError("注册/删除 CNAME")


    def checkip(self,ip):
        '''
        查询IP地域信息
        :param ip: 目标IP
        :return:
        '''
        url = "http://"+Host+"/v1/ipcdninfo/" + str(ip)
        token=self.op.token_of_request(url)

        token="QBox " + token
        header={'Authorization':str(token)}
        re=requests.get(url,headers = header)
        #return  http.get(url,headers=header)
        return re.status_code,re.headers,re.text


    def regionalip(self,cname,isp=None,province=None):

        url = "http://"+Host+"/v1/regionalip/"
        body={}
        body["cname"]=cname
        if isp is not None:
            body["isp"]=isp
        if province is not None:
            body["province"]=province

        body = json.dumps(body)
        print body
        print type(body)
        #print body
        token = self.op.token_of_request(url,body=body)
        token="QBox " + token
        header={'Authorization':str(token)}
        re=requests.post(url,data=body,headers = header)
        #return  http.get(url,headers=header)
        return re.status_code,re.headers,re.text


    def cname(self,cname,sync=False):
        '''
        查询某条CNAME的区域分布
        :param cname:
        :param sync: 默认异步
        :return:区分分布
        '''

        url="http://" + Host + "/v1/cname/" + cname
        if not sync:
            url = url + "?sync=true"

        token=self.op.token_of_request(url)

        token="QBox " + token
        header={'Authorization':str(token)}
        re=requests.get(url,headers = header)
        #return  http.get(url,headers=header)
        return re.status_code,re.headers,re.text


    def dnsmap(self):
        pass

