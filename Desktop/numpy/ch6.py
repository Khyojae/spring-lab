import pandas as pd
from pandas import DataFrame

data = {
"종가": [157000,51300,68800,140000],
"PER": [39.88,8.52,10.03,228.38],
"PBR": [4.38,1.45,0.87,2.16]
}
index = ['NAVER', '삼전', 'LG','카카오']
df = DataFrame (data,index)
print(df)
print("\n")
data = [
    [157000,39.88,4.38],
    [51300,8.52,1.45],
    [68800,10.03,0.87],
    [140000,228.38,2.16]
]
index = ['Naver', '삼전', 'lg', '카카오']
colums =['종가','per','pbr']
df1=DataFrame(data=data,index=index,columns=colums)
print(df1)
print("\n")

data = [
    {"종가": 157000, "per":39.88, "pbr":4.38},
    {"종가": 513000, "per":8.52, "pbr":1.45},
    {"종가": 68800, "per":10.03, "pbr": 0.87},
    {"종가": 14000, "per":228.38, "pbr":2.16}]
index = ['naver','삼전','lg','카카오']
df= DataFrame(data=data, index=index)
print(df)
print("\n")

#연습
data = [
    {"시가": 980, "고가":990, "저가":920, "종가":930},
    {"시가": 200, "고가":300, "저가":180, "종가":180},
     {"시가": 300, "고가":500, "저가":300, "종가":400}
]
index = ['비트코인', '리플', '이더리움']
df2 =DataFrame(data=data,index=index)
print(df2)
