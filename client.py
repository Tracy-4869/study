# -*- codeing = utf-8 -*-
# @Time : 2021/7/29 16:34
# @Author : zang
# @File : client.py
# @Software : PyCharm
import json

import requests

# old = requests.get(('http://127.0.0.1:8087?pass=123'))
# print(old.text)

postdata = {'pass': '123456'}
new = requests.put('http://127.0.0.1:8087', data=postdata)
print(new.text)