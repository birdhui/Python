import random

random_number = random.randint(1, 100)

game_count = 1

while True:
    try:
        my_number = int(input("1부터 100까지의 숫자를 입력하세요:"))

        if my_number > random_number:
            print("다운")
        elif my_number < random_number:
            print("업")
        elif my_number == random_number:
            print(f"축하합니다. {game_count}회 만에 맞췄습니다.")
            break

        game_count = game_count + 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력해주세요.")

    # except문
    # : try문 안의 코드에서 에러가 발생했을 때 except문 실행
    # : 문자를 입력하더라도 예외처리를 하여 종료되지 않는 게임 완성