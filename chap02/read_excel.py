# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('C:/Users/lenovo/Documents/카카오톡 받은 파일/남북한발전전력량.xlsx', engine='openpyxl')   # header=0 (default 옵션)
df2 = pd.read_excel('C:/Users/lenovo/Documents/카카오톡 받은 파일/남북한발전전력량.xlsx', engine='openpyxl', header=None)   # header 옵션 미적용

# 데이터프레임 출력
print(df1)
print('\n')
print(df2)