import pandas as pd
import numpy as np

data = np.array(['a','b', 'c', 'd'])
s = pd.Series(data) # pandas 에서 series 타입 만들기
print(s)
data2 = {'Name' : ['홍길동','김유신','유관순','강감찬'],
        'Age' : [20, 30, 40,50]
        }
df = pd.DataFrame(data2, index=[1,2,3,4])
print(df)