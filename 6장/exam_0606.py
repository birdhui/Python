# 6. 수로 구성된 리스트 nlist  내에 숫자 n이 있는지 판단하는 함수 find_list(nlist, n)을 작성하시오.

nlist = [2, 5, 8, 3]

def find_list(list, n):
    if n in list:           # n이 매개변수 list에 있다면
        return True         # True를 반환
    else:
        return False

res = find_list(nlist, 2)
print(res)