import pandas as pd

# 행 인덱스 / 열 이름 지정해 데이터프레임 만들기
df = pd.DataFrame([[15, '남', '덕여중'], [17, '여', '수리중']], index=['준서', '예은'], columns=['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인
print(df)           # 데이터프레임
print('\n')

# 열 이름 변경
df.rename(columns={'나이': '연령', '성별': '남녀', '학교': '소속'}, inplace=True)

# 행 이름 변경
df.rename(index={'준서': '학생1', '예은': '학생2'}, inplace=True)

# df출력
print(df)