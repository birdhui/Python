# 컴퓨터의 외부 IP주소 확인하는 방법
import requests
import re

req = requests.get("https://ipconfig.kr")
# out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
# print(out_addr)