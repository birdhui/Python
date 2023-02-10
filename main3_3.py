from gtts import gTTS
from playsound import playsound

file_path = r'3. 텍스트를 음성으로 변환\my_text.txt'    # 읽어올 파일의 경로를 바인딩
with open(file_path, 'rt', encoding='UTF8') as f :    # with는 파일을 열고 종료되면 자동으로 파일을 닫는다.
    read_file = f.read()        # 파일의 전체 내용을 읽어 read_file 변수에 바인딩(= 절대 주소)

tts = gTTS(text=read_file, lang='ko')
tts.save(r"3. 텍스트를 음성으로 변환\my_text.mp3")