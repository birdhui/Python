infile = "infile.txt"
outfile = "outfile.txt"

# 파일 읽기
with open(infile, "r") as file:
    line = file.readline()

# 변수 초기화
cnt_a = 0
cnt_e = 0
cnt_i = 0
cnt_o = 0
cnt_u = 0

# 모음 검사 및 개수 카운트
for char in line:
    if char.lower() == "a":
        cnt_a += 1
    elif char.lower() == "e":
        cnt_e += 1
    elif char.lower() == "i":
        cnt_i += 1
    elif char.lower() == "o":
        cnt_o += 1
    elif char.lower() == "u":
        cnt_u += 1

# 결과 출력
with open(outfile, "w") as file:
    file.write("Count of 'a': {}\n".format(cnt_a))
    file.write("Count of 'e': {}\n".format(cnt_e))
    file.write("Count of 'i': {}\n".format(cnt_i))
    file.write("Count of 'o': {}\n".format(cnt_o))
    file.write("Count of 'u': {}\n".format(cnt_u))
