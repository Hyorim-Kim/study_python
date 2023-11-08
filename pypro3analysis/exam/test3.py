import pandas as pd

data = {
    'product':['아메리카노','카페라떼','카페모카'],
    'maker':['스벅','이디아','엔젤리너스'],
    'price':[5000,5500,6000]
}

df = pd.DataFrame(data)
# df.to_sql('test', conn, if_exists='append', index=False)  -- 이게 답
