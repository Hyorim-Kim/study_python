import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3]).reshape(3, 1)

# 연산결과 이유: 브로드캐스팅
print(x + y)
