# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'kor': 100, 'eng': 80, 'math': 90})
student2 = pd.Series({'math': 80, 'kor': 90, 'eng': 80})
print(student1)
print('\n')
print(student2)
print('\n')

# 과목별 점수 사칙연산
add = student1 + student2
sub = student1 - student2
multi = student1 * student2
div = student1 / student2
print(type(div))
print('\n')

# 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
result = pd.DataFrame([add, sub, multi, div], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])

print(result)
