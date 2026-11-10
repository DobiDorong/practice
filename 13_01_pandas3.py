import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_SMALL = 'data/13_diecasting_small.csv'
F_MASTER = 'data/13_diecasting_master.csv'

# 열 골라내기
# - 열 이름
df = pd.read_csv(F_SMALL)
# print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())    # [214.0, 217.0, 215.0]

# 단일 열 선택
# - df["실린더압력"]
# - 결과값은 Series로 나옴
# print(df["실린더압력"])

# 복수 열 선택
# - 여러 열은 이름들을 리스트에 묶어서 넣는다
# - 결과값은 DataFrame으로 나옴
# print(df[['형체력','실린더압력']])

# 실습1
# df_s = pd.read_csv(F_SMALL)
# print(df_s["형체력"].head(3).tolist(), type(df_s["형체력"].head(3)))
# print(type(df_s[["형체력","실린더압력"]]), df_s[["형체력","실린더압력"]].shape)
# print(type(df_s[["형체력"]]))

# 행 선택
# - 라벨과 위치 번호의 차이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번째인지, 항상 0부터 시작

# sorted = df.sort_values("형체력", ascending=False)
# print("정렬 후 인덱스 앞 4개:", sorted.index[:4].tolist())  # 정렬 후 인덱스 앞 4개: [22, 17, 27, 12]
# print("정렬 후 iloc[0] 샷:", int(sorted.iloc[0]['샷'])) # 정렬 후 iloc[0] 샷: 23
# print("정렬 후 loc[0] 샷:", int(sorted.loc[0,'샷']))    # 정렬 후 loc[0] 샷: 1

# 여러 행 선택
# print(df.loc[0:4].shape)    # (5,8) -> 끝번호도 포함해서 출력
# print(df.iloc[0:4].shape)   # (4,8)

# 행, 열 동시 선택
# df.loc[행,열] - 열 이름 사용O / df.iloc[행,열] - 열 이름 사용X -> 숫자로 접근
# print(df.loc[0:4,['실린더압력','형체력']].shape)
# print(df.iloc[0:5,[2,6]].shape)

# 실습2
# df_s = pd.read_csv(F_SMALL)
# print(df_s.loc[0],'\n',"변경 전 첫번째 샷:", df_s.iloc[0]['샷'])
# sorted = df_s.sort_values("형체력", ascending=False)
# print(sorted.loc[0],'\n',"변경 후 첫번째 샷:", sorted.iloc[0]['샷'])

# 실습3
# df_s = pd.read_csv(F_SMALL)
# print(df_s.columns.tolist())
# print(df_s.loc[:4,["실린더압력","형체력"]].shape)
# print(df_s.iloc[:5,[2,6]].shape)

# 실습4
F_SHOT = 'data/13_diecasting_shot.csv'
df = pd.read_csv(F_SHOT)
print(df.shape)
print(df.columns)
sel = df.loc[:9, ["설비ID","비스킷두께","품질등급"]]
back = df.iloc[-5:]
print(sel, back)
