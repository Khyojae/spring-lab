import pandas as pd
from pandas import Series

#브로드캐스팅 (반복문 사용 안해)
data = [100,200,300]
index = ['월', '화', '수']
s = pd.Series(data,index)
print(s+10)

#사칙연산  동일한 인덱스 끼리 뺀다
high = Series([1,2,3,4,5])
low = Series([5,4,3,2,1])
diff = high - low
print(diff)

#비교연산
s=Series(data=[100,200,300,400,500])
cond = s> 300
print(cond)

#연습
lowprice=Series(data=[10,200,200,400,600])
highprice=Series(data=[100,300,400,500,600])
diffprice= (highprice-lowprice)>=100
print(lowprice[diffprice])