#-.- coding:utf-8 -.-
__author__ = 'caeser'
import cdnspider
import pprint
import  json
from resolvespider import *



'''
cdn5.live.cztv.com   CNAME iduwor8.qiniudns.com
cdn5.video.cztv.com  CNAME iduwo5h.qiniudns.com
cdn5.static.cztv.com CNAME iduwo5e.qiniudns.com
'''

op=cdnspider.SpiderMan()



#print op.searchCname("vod3.china.line.qiniudns.com")
#rs = op.register("tiny.china.qiniu.qingcdn.com",POST=True)
#print rs

rs = checkip("125.39.59.19")

#print "CDN服务提供商:"+str(cdn)




#rs = op.regionalip(cname="wsall.qiniu.vod.wscdns.com")
#print rs
'''
#op.cname("tiny.china.qiniu.cloud.cdntip.com")
rs= op.cname("tiny4.china.line.qiniudns.com")

print type(rs[2])
s = rs[2].encode("utf8")
print type(s)
js = json.loads(s)
print type(js)
mjs = js["regional_cname_map"]
print mjs
print type(mjs)
for k in mjs:
    a = k
    ip = mjs[k]
    #print "dict[%s] =" % k,mjs[k]
    children = ip["dns_record_tree"]["root"]["children"]
    for i in children:
        chil1=children[i]
        #print "dict[%s] =" % i,children[i]
        for j in chil1:
            chil2 = chil1[j]
            #print "dict[%s] =" % j,chil1[j]
            for l in chil2:
                ips = chil2[l]["ip_count_map"]
                #print "dict[%s] =" % l,chil2[l]["ip_count_map"]
                #print "[%s] =" % a,ips

                print "%s\t" % a, ",".join([i.encode('utf8') for i in ips.keys()])


'''