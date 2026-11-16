import pandas as pd
import numpy as np

# 그룹 통계와 상관관계
# - 그룹 통계 -> 원본 행과 그룹 기준 비교 -> 두 기준 표 -> 상관관계

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'
F_STD = 'data/14_hydraulic_std.csv'

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# print(round(df["온도"].mean(),2))
# print(round(df["온도"].std(),2))

# print(df.groupby("냉각기상태")["온도"].mean().round(2))
# 냉각기상태
# 고장    54.67
# 저하    45.46
# 정상    35.89
# print(df.groupby("냉각기상태")["온도"].std().round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36

# 분산/표준편차
# v = df.groupby("냉각기상태")["온도"].var()
# std = df.groupby("냉각기상태")["온도"].std().round(2)
# print(v.round(2))
# 냉각기상태
# 고장    14.13
# 저하     2.15
# 정상     0.13
# print(std.round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36
# print((std**2).round(2))
# 냉각기상태
# 고장    14.14
# 저하     2.16
# 정상     0.13

# agg - 여러 통계 한 번에 표로 모으기
# - 리스트: 같은 대상에 여러 통계
# - 딕셔너리: 열별 통계
# - named aggregation: 결과 열의 이름까지 지정

# print(df.groupby("냉각기상태")["온도"].agg(["mean","max","std"]).round(2))
# print(df.groupby("냉각기상태")[["온도","진동"]].agg(["mean","max","std"]).round(2))

# # 이름 붙이기
# summary = df.groupby("냉각기상태").agg(
#     평균온도 = ("온도","mean"),
#     평균진동 = ("진동","mean")
# )
# print(summary)

# # 열별로 다른 통계 목록 지정
# summary2 = df.groupby("냉각기상태").agg({
#     "온도" : ["mean","std"],
#     "진동" : ["mean","max"]
# })
# print(summary2)


# # 실습1
# print(qc["검사결과"].value_counts())
# print(qc.groupby("검사결과")["온도"].agg(["mean","std","max"]).round(2))
# print(qc.groupby("검사결과").agg(
#     평균온도 = ("온도","mean"),
#     평균냉각효율 = ("냉각효율","mean"),
#     측정수 = ("검사결과","count")
# ).round(2))

# transform - 그룹 통계를 원래 행에 붙이기
# - 원래 행 인덱스와 모양을 유지한다

# 같은 그룹의 평균 붙이기
# print(df.groupby("냉각기상태")["온도"].mean().shape)    #(3,)
# print(df.groupby("냉각기상태")["온도"].transform("mean").shape) #(120,)

# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# print(marked[["냉각기상태","온도","그룹평균","편차"]].head(3).round(2))

# pivot_table - 두 기준 표를 한 번에
# - margins = True -> 전체 집계 추가
# - 값이 없는 조합의 평균이 0으로 메우지 않도록

# temp_table = pd.pivot_table(df, index="밸브상태",columns="운전부하"
#                             ,values=["온도"], aggfunc=["mean"], 
#                             margins=True, margins_name="전체")
# - index: 결과표의 행을 나누는 기준
# - columns: 결과표의 열을 나누는 기준
# - values: 각 칸에서 계산할 측정값
# - aggfunc: 그 측정값으로 요약
# - margins=True: 전체 집계 행, 열 추가
# = marggins_name: 추가 집계 이름 표시

# print(temp_table.round(2))

# 실습2
# df = pd.read_csv(F)
# trans = df.copy()
# trans["온도평균"] = trans.groupby("냉각기상태")["온도"].transform("mean")
# trans["편차"] = trans["온도"]-trans["온도평균"]
# print(trans.head(3))
# print("절대값 최대 행의 편차:",trans["편차"][trans["편차"].
#                                   abs() == trans["편차"].abs().max()]
#                                   .to_string(index=False))
# temp_table = pd.pivot_table(df, index="밸브상태", columns="운전부하",
#                             values="온도", aggfunc="mean",
#                             margins=True, margins_name="전체 평균")
# print(temp_table, temp_table.shape)

# corr - 두 지표의 상관계수 구하기
# print(round(df["온도"].corr(df["진동"]), 3)) # 0.931
# print(round(df["온도"].corr(df["압력"]), 3)) # 0.284
# print(round(df["온도"].corr(df["냉각효율"]), 3)) # -0.951

# 실습3
# print(round(df["온도"].corr(df["진동"]),3))
# print(round(df["온도"].corr(df["압력"]),3))
# print(round(df["온도"].corr(df["냉각효율"]),3))
# cor = round(df[["온도","압력","진동","냉각효율"]].corr(),3)
# mask = np.triu(np.ones(cor.shape, dtype=bool), k=1)
# pairs = cor.where(mask).stack()
# print(pairs)
# strongest = pairs.abs().idxmax()
# weakest = pairs.abs().idxmin()
# print("가장 강한 짝:", strongest, pairs.loc[strongest])
# print("가장 약한 짝:", weakest, pairs.loc[weakest])

# print("가장 강한 짝:", cor.loc["온도","냉각효율"])
# print("가장 약한 짝:", cor.loc["압력","냉각효율"])

# 실습4
# print(qc.columns)
# cor = round(qc[["온도", '진동', '압력', '냉각효율', '유량', '모터전력',
#                 '효율지수', '보조압력', '냉각출력', '배유온도']].corr(),3)
# mask = np.triu(np.ones(cor.shape, dtype=bool), k=1)
# print(mask.sum())
# pairs_table = cor.where(mask)
# # print(pairs_table)
# print(pairs_table[pairs_table.abs() >= 0.4].count().sum())
# over = pairs_table[pairs_table.abs() >= 0.95]
# print(over.count().sum())
# # print(over.count().sum())
# top = over.unstack().dropna().reindex(
#     over.unstack().dropna().abs().sort_values(ascending=False)
#     .index).head(5)
# # print(over.unstack().dropna())
# print(top)
# # print(over)

# 실습5
df = pd.read_csv(F)
s = pd.read_csv(F_STD)
m_left = df.merge(s, on="냉각기상태", how="left")
print(m_left.shape, m_left.info())
band = pd.cut(m_left["온도"],bins=[0,40,50,200],
              labels=["낮음","보통","높음"],right=True)
print(band.value_counts())
summary = m_left.groupby("냉각기상태").agg(
    측정수 = ("냉각기상태","count"),
    평균온도 = ("온도","mean"),
    온도표준편차 = ("온도","std"),
    평균냉각효율  = ("냉각효율","mean"),
    위험도 = ("위험도", "mean"),
    점검주기 = ("권장점검주기", "mean")
).round(2)
print(summary)
m = m_left.copy()
m["온도구간"] = band
print(pd.crosstab(m["냉각기상태"],m["온도구간"]))
print(round(m["온도"].corr(m["냉각효율"]), 3)) 
print(round(m["온도"].corr(m["진동"]), 3)) 
m["평균온도"] = m.groupby("냉각기상태")["온도"].transform("mean").round(2)
sorted_m = m.sort_values(by=["위험도","평균온도"],ascending=[False,False])
print(sorted_m.head(3))