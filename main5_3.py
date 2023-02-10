# 1초당 반복해서 정보를 출력하는 코드 만들기
# 1초에 한 번씩 반복해 CPU의 사용량, 사용 가능한 메모리, 네트워크 사용량을 출력하는 코드

import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    # CPU의 사용량을 1초 동안의 평균값을 구한다.
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'CPU사용량: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1)
    print(f'사용 가능한 메모리: {memory_avail}GB')

    net = psutil.net_io_counters()
    # 현재(curr_sent) 측정한 값에서 이전에(prev_sent) 측정한 값을 빼면 1초 동안 보내는 데이터를 구할 수 있음.
    curr_sent = net.bytes_sent/1024**2
    # 현재(curr_sent) 측정한 값에서 이전에(prev_sent) 측정한 값을 빼면 1초 동안 받은 데이터를 구할 수 있음.
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent-prev_sent,1)
    recv = round(curr_recv-prev_recv,1)

    print(f'보내기: {sent}MB 받기: {recv}MB')

    # 이전의 값에 현재 값을 바인딩
    # 이전의 값을 가지고 있어야 현재값과 비교하여 1초 동안 얼마를 보내고 받았는지 계산할 수 있음
    prev_sent = curr_sent
    prev_recv = curr_recv

    # 자동으로 출력되는 값을 종료시 : Ctrl + C