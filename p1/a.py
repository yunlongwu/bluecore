#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json



headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",


}
html = requests.get("http://www.bluecore.com.cn",headers=headers)

print(html.text)
with open("/home/python/Desktop/bluecore/hrcode/p1/new.html","w",encoding='UTF-8') as f:
   f.write(html.text)

