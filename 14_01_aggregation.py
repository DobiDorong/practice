import pandas as pd

F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'
F_STD = 'data/14_hydraulic_std.csv'


# 빈도와 그룹 집계
# - 값별로 세기와 그룹별로 집계하기

df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
# print(df.shape,qc.shape)    # (120, 8) (200, 11)


# 1. 빈도
# - value_counts
# - pd.cut

# print(df['냉각기상태'].value_counts())
# 냉각기상태
# 고장    40
# 저하    40
# 정상    40
# Name: count, dtype: int64

# print(df['밸브상태'].value_counts())
# 밸브상태
# 정상    61
# 지연    20
# 경미    20
# 심각    19
# Name: count, dtype: int64

# 개수 -> 비율 : normalize
# counts = df["result"].value_counts()
# ratios = df["result"].value_counts(normalize=True)
# print(counts)
# print(ratios.round(3))
# print((ratios*100).round(1))

# 실습1
# df = pd.read_csv(F)
# print(df.shape)
# valv = df["밸브상태"].value_counts()
# valv_ratio = df["밸브상태"].value_counts(normalize=True)
# print(valv.round(2), (valv_ratio*100).round(2))
# oper = df["운전부하"].value_counts()
# oper_ratio = df["운전부하"].value_counts(normalize=True)
# print(oper.round(2), (oper_ratio*100).round(2))
# for counts in [valv_ratio, oper_ratio]:
#     print("가장 많은 값:", counts[counts == counts.max()])
#     print("가장 적은 값:", counts[counts == counts.min()])

# pd.cut
# band = pd.cut(df["온도"],bins=[0,40,50,200], labels=["낮음","보통","높음"],right=True)
# print(band.value_counts(sort=False))

# # 실습2
# qc = pd.read_csv(F_QC)
# print(qc.shape)
# counts = qc["검사결과"].value_counts()
# print(counts)
# counts_ratio = qc["검사결과"].value_counts(normalize=True)
# print(counts_ratio.round(3))
# print("불합격이 전체의 약",(counts_ratio*100)["불합격"].round(3),"%")

# 실습3
# df = pd.read_csv(F)
# vib_max = df["진동"].max()
# vib_min = df["진동"].min()
# print(vib_max, vib_min)
# bound = pd.cut(df['진동'],bins=[0,0.6,0.7,10],
#                labels=["약함","보통","강함"],right=True)
# print(bound.value_counts(sort=False).to_string(),
#       "\n구간 미지정 개수:",bound.isna().sum())
# bound_1 = pd.cut(df['진동'],bins=[0,0.62,0.7,10],
#                labels=["약함","보통","강함"],right=True)
# bound_count = bound.value_counts()
# bound_1_count = bound_1.value_counts()
# def max(a):
#     print(a[a == a.max()])
# def min(a):
#     print(a[a == a.min()])
# max(bound_count),min(bound_count)    
# max(bound_1_count),min(bound_1_count)    

# 그룹 집계
# - 분할 -> 적용 -> 결합 구조
# - groupby

# means = df.groupby("냉각기상태")["온도"].mean()
# print(means.round(2))

# print(df.groupby("냉각기상태")["온도"].max())


# # 여러 키 그룹 코드
# keys = ["냉각기상태","운전부하"]
# print(df.groupby(keys)["온도"].mean().round(2))

# # crosstab
# print(pd.crosstab(df["냉각기상태"],df["운전부하"]))

# 실습4
# df = pd.read_csv(F)
# cy = df["냉각기상태"].value_counts()
# mean = df.groupby("냉각기상태")["온도"].mean().round(2)
# t = mean.max()-mean.min()
# m = df.groupby("냉각기상태")["온도"].max().round(2)
# print(cy,mean,"차이",t,m)

# 실습5
df = pd.read_csv(F)
val = df["밸브상태"].value_counts()
print(val)
p = df[df["result"] == "고장"]
p_counts = p.groupby("밸브상태").size()
print(p_counts)
# 고장 라벨이 0건인 상태도 빠지지 않도록 이름표를 맞춘다
p_counts = p_counts.reindex(val.index, fill_value = 0)
ratios = p_counts / val
print(ratios.sort_values(ascending=False).round(3))

