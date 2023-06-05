word = input("단어를 입력하시오: ")

alphabet_count = 0
number_count = 0

for char in word:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        number_count += 1

print("알파벳 문자 개수:", alphabet_count)
print("숫자 개수:", number_count)
