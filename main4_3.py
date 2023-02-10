import qrcode

file_path = r'4. QR코드 생성기\QR코드모음.txt'
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

        # 12 ~ 16: 읽어온 데이터로 QR코드 생성
        qr_data = line
        qr_img = qrcode.make(qr_data)

        save_path = '4. QR코드 생성기\\' + qr_data + '.png'
        qr_img.save(save_path)