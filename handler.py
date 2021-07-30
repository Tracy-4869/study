# -*- codeing = utf-8 -*-
# @Time : 2021/7/29 17:29
# @Author : zang
# @File : handler.py
# @Software : PyCharm

def exist_query(route):
    query = {}
    route = route.split('?')
    if len(route) == 1:
        return route[0], query
    params = route[1].split('&')
    for param in params:
        k, v = param.split('=')
        query[k.strip()] = v.strip()
    return route[0], query

def parse_firstline(rbuff):
    request_line = rbuff.readline()
    method, route, http_version = request_line.decode().strip().split()
    route, query = exist_query(route)
    return query

def parse_headers(rbuff):
    headers = {}
    data = rbuff.readline()
    while True:
        header = rbuff.readline()
        head = header.decode().split(':')
        if len(head) == 1:
            break
        k, v = head
        headers[k.strip()] = v.strip()
    return headers

def exist_body(rbuff, headers):
    body = {}
    key = 'Content-Length'
    if key not in headers:
        return body
    content_length = int(headers[key])
    data = rbuff.read(content_length)
    params = data.decode().split('&')

    for param in params:
        k, v = param.split('=')
        body[k.strip()] = v.strip()
    return body