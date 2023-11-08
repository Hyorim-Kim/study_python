import pandas as pd
import numpy as np

data = {
    'juso': ['강남구 역삼동', '중구 신당동', '강남구 대치동'],
    'inwon': [23, 25, 15]
}

df = pd.DataFrame(data)
results = pd.Series([x.split()[0] for x in df.juso])
print(results)

print()
df = pd.DataFrame([[1.4, np.nan], [7, 4.5], [np.NaN, np.NAN], [0.5, -1]])
print(df.dropna())
