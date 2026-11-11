import pandas as pd
import numpy as np

F_SHOT = 'data/13_diecasting_shot.csv'
F_SMALL = 'data/13_diecasting_small.csv'
F_MASTER = 'data/13_diecasting_master.csv'

df = pd.read_csv(F_SHOT)

# 조건 필터링과 정렬
# df = pd.read_csv(F_SHOT)
# print(df.shape)

# 배열에서 하던 것
# arr = df["비스킷두께"].values
# print("배열에서 조건 참 개수:", int((arr >= 16).sum()))     # 74

# 표에서 하는 것
# print("표에서 조건 참 개수:", int((df['비스킷두께']>=16).sum()))    #74

# 조건 -> boolean Series
# s = df['비스킷두께'] >= 16
# print(s.head(3).tolist())   # [False, False, False]

# print(int(df['비스킷두께'].isna().sum()))
# print(int((df['비스킷두께'] < 16).sum()))

# 실습1
# df = pd.read_csv(F_SHOT)
# print(df.shape)
# a = int((df["비스킷두께"]>=16).sum())
# b = int((df["비스킷두께"]<16).sum())
# print("16 이상:",a,"16 미만:",b,"합계:", a+b)
# print("총 열:",len(df['비스킷두께']))
# print("결측:",len(df['비스킷두께'])-a-b)

# 복합 조건
# df = pd.read_csv(F_SHOT)
# both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
# either = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 25)]
# print(len(both), len(either))

# 부정 조건 : ~
# print(len(df[~(df["품질등급"] == "불량")]))

# isin : 값이 포함되어 있는지
# print(len(df[df["품질등급"].isin(["주의","불량"])]))    # |(또는) 사용과 같은 결과

# between : 사이를 의미(양쪽 경계 모두 포함)
# print(len(df[df["비스킷두께"].between(10,16)]))

# 문자열 조건
# 숫자열에는 쓸 수 없음
# - str.contains: 해당 문자열을 포함하는 값
# print(len(df[df["설비ID"].str.contains("A")]))  # A가 포함된 값 = A라인 전체


# - str.split, str.replace, str.strip...
# print(df["설비ID"].head(1).tolist())    # ['DIE-A-01']
# print(df["설비ID"].str.split("-").head(1).tolist())     # [['DIE', 'A', '01']]
# print(df["설비ID"].str.split("-").str[0].head(1).tolist())

# 실습2
# df = pd.read_csv(F_SHOT)
# print(len(df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]))
# print(len(df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 25)]))
# print(len(df[~(df["품질등급"] == "불량")]))

# 실습3
# df = pd.read_csv(F_SHOT)
# print(len(df[df["품질등급"].isin(["주의","불량"])]))
# print(len(df[df["비스킷두께"].between(10,16)]))
# print(len(df[df["설비ID"].str.contains("A")]))
# print(len(df[(df["설비ID"].str.contains("A.*01"))]))    # A.*01 는 A가 먼저 나오고 중간은 상관없이 뒤에 01이 나오는 모든 값을 찾는 것

# 정렬, 복사본
# 정렬 - sort_values
# - 기본값은 작은 값부터인 오름차순
# - 한 열로 정렬해도 모든 열이 행 단위로 함께 이동한다
# asc = df.sort_values("비스킷두께")
# print(asc["비스킷두께"].head(3).tolist())   # [2.0, 2.0, 4.0]

# # 내림차순
# dec = df.sort_values("사이클타임", ascending=False)
# print(dec["사이클타임"].head(3).tolist())   # [6170.0, 652.3, 125.9]

# # 다중 키 정렬
# two = df.sort_values(["품질등급","비스킷두께"],ascending=[True,  False])
# print(two.head())   # 품질등급으로 오름차순 후 그 안에서 비스킷두께로 내림차순
# print(two["샷"].head(3).tolist())

# # copy
# x = df[df["품질등급"] == "불량"].copy()
# print(x.shape)  # (20, 8)
# x["위험등급"] = "높음" # 없는 열 추가
# print(x.shape)  # (20, 9) -> 열 1개 추가됨

# 실습4
# df = pd.read_csv(F_SHOT)
# print((df.sort_values("비스킷두께",ascending=False).head(5))["샷"].tolist())
# print((df.sort_values(["품질등급","사이클타임"], ascending=[True,False]).head(5))["샷"].tolist())
# print(df["샷"].head().tolist())

# 실습5
df = pd.read_csv(F_SHOT)
con = df[((df["품질등급"] != "양품")) & (df["비스킷두께"] >= 16)]
print(len(con))
sort_df = con.sort_values("비스킷두께",ascending=False)
report = sort_df[["설비ID","비스킷두께","품질등급"]]
print(report.head(3))
#      설비ID  비스킷두께 품질등급
# 197  DIE-A-01   27.0   불량
# 191  DIE-B-01   26.0   불량
# 42   DIE-A-01   21.0   주의

# 결측 때문에 제외된 양품 아닌 샷 확인
print(df["비스킷두께"][~(df["품질등급"] == "양품")].isna().sum())