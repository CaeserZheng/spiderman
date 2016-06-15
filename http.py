__author__ = 'caeser'
#-.- coding:utf-8 -.-

import requests


def get(url,headers=None,body=None):

    #print header
    re=requests.get(url,headers=None,body=None )

    try:
        re=requests.get(url,headers = headers)
        if re.status_code == 200:
            res = re.text
            return
        else:
            print(re.status_code,re.headers,re.text)

    except:
        print(re)



