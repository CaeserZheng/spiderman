#-.- coding:utf-8 -.-
__author__ = 'caeser'
import utils
import pprint
import  json



'''
cdn5.live.cztv.com   CNAME iduwor8.qiniudns.com
cdn5.video.cztv.com  CNAME iduwo5h.qiniudns.com
cdn5.static.cztv.com CNAME iduwo5e.qiniudns.com
'''

op=utils.SpiderMan()

#rs = op.register("tiny.china.qiniu.qingcdn.com",POST=True)
#print rs

rs = op.checkip("183.131.160.111")
print rs[2]

#rs = op.regionalip("wsall.qiniu.dl.wscdns.com","电信","北京")
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