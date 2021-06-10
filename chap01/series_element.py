import pandas as pd

# 튜플을 시리즈로 변환 (인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름', '생년월일', '성별', '학생여부'])
print(sr)

# 원소 1개 선택
print(sr[0])
print(sr['이름'])

# 여러개의 원소 선택
print(sr[[1, 2]])
print('\n')
print(sr[['생년월일', '성별']])

# 여러개의 원소 선택 (인덱스 범위 지정)
print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])