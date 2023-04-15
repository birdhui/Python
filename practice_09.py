# 답: 1
height = 182
weight = 93

# height가 180보다 크고 weight가 90보다 작다면 => False지만 논리 부정 not이 붙었기 때문에 True => mem = 1이 된다.
if not (height > 180 and weight < 90):
    mem = 1
else:
    mem = 0

print(mem)