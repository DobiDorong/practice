import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)

# 결측 처리
# - 종류: NaN, None, NA, NaT
#   - 표현은 달라도 isna()로 결측 여부 확인 가능

# s = pd.Series([10, None, 20])
# print(s.mean())     # 15.0 -> NaN 값이 있다고 해서 계산이 멈추지 않음
# print(s+1)  # 11.0 NaN, 21.0
# print(s.isna())

# 실습1
# log = pd.read_csv(F_LOG)
# print(log.shape)
# log_nan = log.isna().sum()
# print(log_nan, "총 결측치 갯수:",log_nan.sum())
# pre = (log["사출압력"].eq(0)).sum()
# scr = (log["스크루속도"].eq(-999)).sum()
# bar = (log["배럴온도"].eq(999)).sum()
# print("사출압력:",pre,"스크루속도:",scr,"배럴온도:",bar)

# 실습2
# df = pd.read_csv(F_PROC)
# print(df.shape,df.head(3))
# print(df.info())
# print(df["최대사출속도"].describe().round(3))

# 실습3
# log = pd.read_csv(F_LOG)
# print(log.isna().sum().sum())
# NA_RULES = {
# '배럴온도': [999],
# '스크루속도': [-999],
# }
# log = pd.read_csv(F_LOG, na_values=NA_RULES)
# print(log.isna().sum().sum())
# NA_RULES = {
# '배럴온도': [999],
# '사출압력': [0],
# '스크루속도': [-999],
# }
# log = pd.read_csv(F_LOG, na_values=NA_RULES)
# print(log.isna().sum().sum(), log.isna().sum())

# 실습4
# df = pd.read_csv(F_PROC)
# count = df.isna().sum()
# print(count)
# ratio = count/len(df)*100
# summary = pd.DataFrame({'결측개수': count, '결측률_%': ratio})
# missing_summary = summary.loc[summary['결측개수']>0].copy()
# print(missing_summary.round(1).to_string())
# print(len(missing_summary))

# 실습5
# df = pd.read_csv(F_PROC)
# count = df.isna().sum()
# ratio = count/len(df)*100
# print(ratio.sort_values(ascending=False, kind = "stable").head(3))
# row_m = df[(df.isna().sum(axis=1))>0]
# row_r = df[(df.isna().sum(axis=1)) == 0]
# print("결측이 있는 행:",len(row_m), "정상 행:",len(row_r))
# missing = df.loc[(df.isna().sum(axis=1)) >= 5]
# print(len(missing))
# print("결측이 5개 이상인 행:",len(df[(df.isna().sum(axis=1)) >= 5]))

# 실습6
# df = pd.read_csv(F_PROC)
# s = df["최대사출속도"].isna()
# t = df["감압시간"].isna()
# print(df.head(10).loc[s.head(10)].index, 
#       df.head(10).loc[t.head(10)].index)
# print(s.sum(),t.sum())
# d = df[s & t]
# print("동시 결측된 행:",int(s&t.sum()),"비율:",round(s&t.mean()*100),1)
# print(d[["측정시각", "사출기"]])
# print("한 열만 빈 행:", (len(df[s & ~t]) + len(df[~s & t])))
# print("모두 관측된 행:", len(df[~(s&t)]))

# 실습7
df = pd.read_csv(F_PROC)
ratio = df.isna().mean()
missing_col = ratio[ratio > 0].sort_values(ascending=False)
print(missing_col)