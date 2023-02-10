# 조금 더 정확하게 내부 IP주소를 확인하는 방법

import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.com", 443))    # https의 기본 접속 포트 -> 443
print(in_addr.getsockname()[0])