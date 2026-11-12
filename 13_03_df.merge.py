import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'
F_SMALL = 'data/13_diecasting_small.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

# print(log.shape)
# print(master.shape)

# three = log.head(3)[["샷","설비ID","비스킷두께"]]
# print(three.to_string(index=False))

# merge
# print(three.merge(master, on="설비ID").to_string(index=False))
#  샷 설비ID  비스킷두께 라인  도입연도  정격형체력 담당반
#  1 DIE-A-01   10.0  A  2018    280  1반
#  2 DIE-B-01   11.0  B  2020    320  2반
#  3 DIE-B-01   11.0  B  2020    320  2반
#  master 그래프 안에 three를 같은 키에 맞춰서 넣는다

# merge 기본 사용법
# - on: 두 표를 잇는 키 열, 공통된 키가 없으면 불가
# - 행은 예측불가, 열 수는 예측 가능

# how: 어느 쪽을 다 남길 것인가
# - (기본) how = 'inner'
# - how = 'left': 왼쪽은 다 남기고 짝 없으면 빈 칸
# - how = 'outer': 양쪽 다 남김 

# m_inner = log.merge(master, on="설비ID")
# m_left = log.merge(master, on="설비ID", how="left")
# m_outer = log.merge(master, on="설비ID",how="outer")
# print(m_inner.shape, m_left.shape, m_outer.shape)

# 실습1
# print(log.shape)
# print(master.shape)
# print(log.columns,master.columns)
# m = log.merge(master, on="설비ID")
# print(m.shape)
# print(m.head(2))

# 합치기 전후 점검 코드
# print(len(log)) # 200
# print(len(master),master["설비ID"].nunique())   # 5 5

# m_left = log.merge(master, on="설비ID", how = "left")
# print(len(m_left))  # 200
# print(int(m_left["라인"].isna().sum())) # 15 (데이터가 비어있는 행 개수)

# unmatched = m_left[m_left["라인"].isna()]
# print(unmatched["설비ID"].head(1).tolist(), len(unmatched)) # ['DIE-C-01'] 15

# 실습2
# m = log.merge(master, on="설비ID")
# m_left = log.merge(master, on="설비ID", how="left")
# m_outer = log.merge(master, on="설비ID", how = "outer")
# print(m.shape, m_left.shape, m_outer.shape)
# # 대장에 C 코드 없음
# unmatched = m_left[m_left["라인"].isna()]
# print(len(unmatched),unmatched["설비ID"].head(1).tolist())
# # print(log.isna().sum())
# unmatched_out = m_outer[m_outer["품질등급"].isna()]
# print(unmatched_out["설비ID"].tolist())

# merge는 옆으로 칸을 이어 붙이고, concat은 아래로 줄을 쌓는다
# concat은 키 열이 필요 없고, 칸 이름만 맞으면 된다

# pd.concat

# ex) 설비 로그를 1차, 2차로 나눠 받은 경우
# part1 = log.iloc[:100].reset_index(drop=True)
# part2 = log.iloc[100:].reset_index(drop=True)
# print(part1.shape, part2.shape)     # (100, 8) (100, 8)

# stacked = pd.concat([part1, part2])
# print(stacked.shape)    # (200, 8)
# print(stacked.index[-3:].tolist())  # [97, 98, 99]
# print(len(stacked.loc[[0]]))    # 2

# - 번호를 다시 매기기 -> ignore_index
# renumbered = pd.concat([part1,part2], ignore_index=True)
# print(int(renumbered.index[-1]))    # 199

# - 칸(열)이 다른 표를 붙이면 -> 빈 칸
#   붙이기 전에 두 표의 columns 비교
#   -> set(표1.columns) - set(표2.columns)

# 실습3
# log = pd.read_csv(F_SHOT)
# part1 = log.iloc[:100].reset_index(drop=True)
# part2 = log.iloc[100:].reset_index(drop=True)
# stacked = pd.concat([part1,part2])
# print(stacked.shape, stacked.loc[[0]])
# stacked = pd.concat([part1,part2],ignore_index=True)
# print(stacked.index[-1])

# 실습4
log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)
total = log.merge(master, on="설비ID", how="left")
print(total.columns.tolist())
print(total["라인"].value_counts())
unmatched = total[(total["라인"].notna())]
print(unmatched.shape)
qual = unmatched[unmatched["품질등급"] != "양품"]
print(qual.shape)
print(qual.sort_values("비스킷두께",ascending=False)
      [["샷","설비ID","라인","비스킷두께","품질등급"]].head().to_string(index=False))
