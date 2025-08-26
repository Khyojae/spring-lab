import pandas as pd
data = [100,200,300]
index = ['월', '화', '수']
s = pd.Series(data,index)

#추가하기
s.loc['목']= 400
print(s)

#삭제하기
#변수를 새로 만들어야함
s1=s.drop('목')
print(s1)

#수정하기
data = [100,200,300]
index = ['월', '화', '수']
s = pd.Series(data,index)
s.iloc[0]=1000  #평소에 하던 수정
s.loc["수"]=3000
print(s)