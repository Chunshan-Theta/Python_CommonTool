#-*-coding:utf-8-*-
import json

f = open("JsonData.json", 'r')
b_str = f.read()
f.close()
GpioConfig = json.loads(b_str,encoding='utf-8')
t='早安'
u = unicode(t, "utf-8")
print type(u)
for key, value in GpioConfig.iteritems():
    print key,type(key)
    print GpioConfig[u]
