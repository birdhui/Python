import matplotlib.pyplot as plt
import numpy as np

# 랜덤함수에서 항상 같은 값이 나오게 함
# np.random.seed(임의동일숫자)
np.random.seed(100)
x = np.random.normal(50, 10, size=1000)
plt.hist(x, bins=100)
plt.show()