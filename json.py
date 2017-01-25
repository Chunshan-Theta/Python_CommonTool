#-*-coding:utf-8-*-
import json

#read json file 
f = open("JsonData.json", 'r')
b_str = f.read()
f.close()

#loading json
GpioConfig = json.loads(b_str,encoding='utf-8')

#call data using chinese key
u = unicode('早安', "utf-8")
print GpioConfig[u]

# print all key and data
for key, value in GpioConfig.iteritems():
    print key,type(key)
    print GpioConfig[u]
    
# conbine two array

GpioConfig_b  = json.loads('{"安安":"哈摟"}')
c = dict(GpioConfig_a.items() + GpioConfig_b.items())

for key, value in GpioConfig.iteritems():
    print key,type(key)
    print GpioConfig[u]
