# 가변인수 중에서 가장 큰 수를 반환하는 함수 get_max(*nums)를 작성하는 프로그램
    
def get_max(*nums):
    return (max(nums))      # max 함수 사용
    # max = nums[0]
    # for i in nums:
    #     if i > max:
    #         max = i
    #     return max

mx = get_max(1, 4, 9, 5)
print("최대값: ", mx)
