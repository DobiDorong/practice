import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df = pd.read_csv(F_PROC)
log = pd.read_csv(F_LOG)

# dropna : 행 삭제, 열 삭제
# -axis: 제거할 축을 선택, axis=1 -> 열 전체가 빠지게 됨
# rows_removed = df.dropna()
# cols_removed = df.dropna(axis=1)
# print(rows_removed.shape)   # (76, 22)
# print(cols_removed.shape)   # (250, 10)
# print(df.shape)     # (250, 22)


# - how : 하나라도 비면, 전부 비면
# = any, all
# print(df.dropna(how="any").shape)   # (76, 22)
# print(df.dropna(how="all").shape)   # (250, 22)

# - thresh : 유효값 최소 개수
# print(df.dropna(thresh=20).shape)   # (162, 22)

# - subset : 중요한 열만 검사
#   - 다른 열의 결측이 남아 있어도 지정한 조건을 충족하면 유지한다
# print(df.dropna(subset=['배럴온도1']).shape)

# 실습1
# print(df.shape)
# print(df.dropna().shape)
# print(df.dropna(axis=1).shape)

# 실습2
# print(df.dropna(how="all").shape)
# print(df.dropna(thresh=20).shape)
# print(int(df["불량여부"].isna().sum()))
# print(df.dropna(subset=["불량여부"]).shape)

# 실습3
# META = ['측정시각','사출기','불량여부']     # 결측치가 없아서 쓰지 않는 열
# feature_cols = [c for c in df.columns if c not in META]
# # feature_cols = []     # 윗 줄을 풀어쓴 것.
# # for c in df.columns:
# #     if c not in META:
# #         feature_cols.append(c)
# feature_rate = df[feature_cols].isna().mean()
# drop_cols = feature_rate[feature_rate >= 0.4].index.tolist()
# print(drop_cols)
# base = df.drop(columns=drop_cols).copy()
# print(base.shape)

# # missing = df.isna().mean()*100
# # print(missing)
# # caution = missing[missing > 40].index.tolist()
# # print(caution)
# # df_stan = df.drop(caution, axis=1).copy()
# # print(df_stan.shape)

# 실습4
# versions = {'원본': df, '행제거':df.dropna(),'thresh20':df.dropna(thresh=20)}
# comparison_rows = []

# for name, frame in versions.items():
#     comparison_rows.append({
#         '방식': name,'행수':len(frame),
#         '손실률_%':(1-len(frame)/len(df))*100,
#         '불량수': int(frame['불량여부'].sum()),
#         '불량비율_%': frame['불량여부'].mean()*100
#     })

# comparison = pd.DataFrame(comparison_rows)
# print(comparison.round(1).to_string(index=False))

# 실습5
# s =df['최대사출압']
# mask =s.isna()  # 결측 위치 저장
# mean_filled = s.fillna(s.mean())
# median_filled = s.fillna(s.median())
# print(s.mean().round(2), s.median().round(2))
# print(int(mask.sum()))

# fill_compare = pd.DataFrame({'평균대체': mean_filled, '중앙값대체': median_filled})
# print(fill_compare.loc[mask].head(3).round(2))  # 기존 결측 위치 확인해서 대체가 됐는지 확인

# ffill, bfill
series_demo = pd.Series([None, 73.0, None, None, 75.0])

# ffill - 앞에서 마지막으로 확인한 값으로 채움
# print(series_demo.ffill().tolist())   # [nan, 73.0, 73.0, 73.0, 75.0]
# - limit: 연속 결측 구간에서 최대 몇 칸을 채울지 정할 수 있음

# bfill - 뒤에서 처음 확인되는 값으로 채움
# print(series_demo.bfill().tolist())   # [73.0, 73.0, 75.0, 75.0, 75.0]

# 실습6
NA_RULES = {'배럴온도': [999], '사출압력': [0], '스크루속도': [-999]}
log = pd.read_csv(F_LOG, na_values=NA_RULES, parse_dates=['측정시각'])
# parse_data = 측정 시각을 날짜와 시간으로 읽도록 한 것
log['측정시각'] = pd.to_datetime(log['측정시각'], errors= 'raise')
# 날짜 ,시간 변환 명시적 확인, 날짜와 시간으로 변환했을때 에러가 있으면 알려달라고 만든 것
unknown = log.loc[log['사출기'].isna()].copy()  # '사출기' 미확인 1행 별도 보관
known = log.loc[log['사출기'].notna()].copy()

known = known.sort_values(['사출기', '측정시각'])
print(len(known),len(unknown))  # 15 1
print(int(log.isna().sum().sum()))  # 10

# 앞의 값으로 채우는 것
candidate = known.groupby("사출기")["배럴온도"].ffill(limit=1)
print(candidate)
# 온도가 실제로 있었던 시각만 표시
observed_at = known['측정시각'].where(known['배럴온도'].notna())
# print(observed_at)
# 마지막으로 온도가 있었던 시각
last_time = observed_at.groupby(known['사출기']).ffill()
# print(last_time)
# 현재 기록의 시각 - 마지막으로 온도를 실제 측정한 시각
gap = known['측정시각'] - last_time
can_fill = (known['배럴온도'].isna() & candidate.notna()
            & gap.le(pd.Timedelta('2min')))

# gap.le(pd.Timedelta('2min'))
# - .le : 이하인지 비교
# - pd.Timedelta('2min') : 2분

# 허용 위치에 온도 넣기
known.loc[can_fill,"배럴온도"] = candidate.loc[can_fill]
# print(int(can_fill.sum()))