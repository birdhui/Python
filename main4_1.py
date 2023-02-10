# QR코드 라이브러리 불러오기
import qrcode

# data 변수 값에 네이버 주소 저장
qr_data = 'wwww.naver.com'
# img 변수 값에 QR코드이미지 생성해 저장
qr_img = qrcode.make(qr_data)

# path 변수 값에 저장될 경로를 바인딩
save_path = '4. QR코드 생성기\\' + qr_data + '.png'
# 이미지 저장
qr_img.save(save_path)