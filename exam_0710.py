dictionary = {}

while True:
    word = input("영어 단어를 입력하세요: ")
    
    if word == '0':
        break
    
    word_length = len(word)
    if word_length not in dictionary:
        dictionary[word_length] = [word]
    else:
        dictionary[word_length].append(word)

print("입력한 단어는 다음과 같습니다.")
print(dictionary)
