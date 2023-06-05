# 5. 수로 구성된 리스트 nlist의 평균값을 구하는 함수 avg_list(nlist)를 작성하시오.
nlist = [2, 5, 8, 3]

def avg_list(list):
    res = sum(list) / len(list)     # sum()함수, len()함수 사용해서 평균값 구하기
    return res

avg = avg_list(nlist)
print("평균은 = ", avg)
