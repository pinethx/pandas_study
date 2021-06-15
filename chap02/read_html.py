# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# HTML 파일 경로 url 변수에 저장
url = 'C:/Users/lenovo/Documents/카카오톡 받은 파일/sample.html'

# HTML 웹페이지의 표 가져와서 데이터프레임으로 변환
tables = pd.read_html(url)

# 표의 개수 확인
print(len(tables))
print('\n')

# tables 리스트의 원소를 iteration 하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

# 파이썬 패키지 정보가 들어 있는 두 번재 데이터프레임을 서낵해 df 변수 저장
df = tables[1]

# 'name' 열을 인덱스로 지정
df.set_index(['name'], inplace=True)
print(df)