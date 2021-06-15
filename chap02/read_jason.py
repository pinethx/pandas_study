# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# read_json() 함수로 데이터프레임 변환
df = pd.read_json('C:/Users/lenovo/Documents/카카오톡 받은 파일/read_json_sample.json')
print(df)
print('\n')
print(df.index)