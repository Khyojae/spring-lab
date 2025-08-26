import pandas as pd
arr = [0,1,2,3]
data = [100,200,300]
index = ['월', '화', '수']

s=pd.Series(data, index)
print(s)

a = pd.Series(arr)
print(a)

print(s.index)
print(s.values)