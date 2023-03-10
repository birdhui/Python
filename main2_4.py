import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("wwww.google.co.kr", 443))
print("내부 IP : ", in_addr.getsockname()[0])

# 외부 IP주소가 잘 안됨
req = requests.get("https://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',req.text)[1]
print("외부 IP: ", out_addr)