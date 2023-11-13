# Advertising.csv 파일을 읽어 tv,radio,newspaper 간의 상관관계를 파악하시오. 
# 그리고 이들의 관계를 heatmap 그래프로 표현하시오. 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic')

data = pd.read_csv('../testdata/Advertising.csv')
print(data.head(3), data.shape)

df = pd.DataFrame(data, columns=('tv','radio','newspaper'))
print(df.head(3))

print('\n상관계수')
print(df.corr(method='pearson'))
# tv, radio : 0.054809
# tv, newspaper : 0.056648
# radio, newspaper : 0.354104

print('\nheatmap')
import seaborn as sns
sns.heatmap(df.corr())
plt.show()
