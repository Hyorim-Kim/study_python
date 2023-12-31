# 표준 편차, 분산의 중요성 : 평균은 같으나 분산이 다름으롶 인해 전체 데이터의 분포상태가 달라진다.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

np.random.seed(1)
print(stats.norm(loc = 1, scale = 2).rvs(10))  # 기댓값, 표준편차, 변수의 개수

print('---------------')
centers = [1, 1.5, 2]
col = 'rgb'

std = 2
datas = []

for i in range(3):
    datas.append(stats.norm(loc = centers[i], scale = std).rvs(100))
    plt.plot(np.arange(100) + i * 100, datas[i], '*', color=col[i])

plt.show()
