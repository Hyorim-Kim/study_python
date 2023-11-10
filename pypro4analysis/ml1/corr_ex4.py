# Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 
# 파일질라 참고 25라인부터

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')
import json

data = pd.read_csv('../testdata/Advertising.csv')
print(data.head(3), data.shape)

print()
# 상관계수
print(data.corr(method='pearson'))
# tv, radio : 0.054809
# tv, newspaper : 0.056648
# radio, newspaper : 0.354104

# heatmap
import seaborn as sns
sns.heatmap(data.corr())
plt.show()
