import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()      # f.readlines()로 파일을 읽어 줄 별로 리스트의 값의 형태를 내어준다.

    for line in read_lines:
        line = line.strip()         # line.strip() : 줄 마지막에 줄바꿈 문자 삭제
        print(line)