import pandas as pd
data = [100,200,300]
index = ['월','화','수']
s= pd.Series(data,index)

#index
print(s.iloc[0])
print(s.iloc[2])
print(s.iloc[-1])
print(s.loc['월'])

# 슬라이싱
print(s.iloc[0:2])
print(s.loc["월":"화"])

#여러 값 인덱싱
m=[1,2,3,4]
print(s.iloc[[0,2]])