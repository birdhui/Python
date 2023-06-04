my_dict = {}

while True:
    key = input("영어 단어를 입력하시오: ")
    if key == 'q':
        print(my_dict)
        break

    if key in my_dict:
        print("이미 존재합니다. 다시 입력하시오.")
        continue

    val = input("한글 뜻을 입력하시오: ")
    my_dict[key] = val