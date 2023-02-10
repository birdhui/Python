import socket

in_addr = socket.gethostbyname(socket.gethostname())

print(in_addr)

'''

    socket
    : 외부 사이트에 접속하여 접속된 정보를 바탕으로 IP주소 확인

'''