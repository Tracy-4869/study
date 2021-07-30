# -*- codeing = utf-8 -*-
# @Time : 2021/7/29 16:34
# @Author : zang
# @File : server.py
# @Software : PyCharm

import socket, handler

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8087))

sock.listen(5)

print('开始监听')

#阻塞等待连接，返回请求对象和地址
req, addr = sock.accept()
print('接收到来自 {}:{} 的请求'.format(addr[0], addr[1]))

file = req.makefile('rb')
# line = file.readline()
query = handler.parse_firstline(file)
# respon = query['pass']

headers = handler.parse_headers(file)
# print(headers)

body = handler.exist_body(file, headers)
print(body)
respon = body['pass']

response = b"HTTP/1.1 200 OK\r\n"
response += b"Content-Length: 20\r\n"
response += b'\r\n'
response += respon.encode('utf-8')

req.send(response)












