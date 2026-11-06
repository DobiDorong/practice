import numpy as np


F = 'data/11_diecasting_series.csv'

# ct = np.genfromtxt(F,delimiter=",",skip_header=1,usecols=1)
# print(ct.shape, ct.size)

def col(c) :
    return np.genfromtxt(F,delimiter=",",skip_header=1,usecols=c)

# 자리 찾기
# fancy indexing

# vib = np.array([2.1, 2.3, 2.0, 5.8])
# pick = np.array([0, 3])
# print(vib[pick])    # [2.1 5.8]

# 정렬과 정렬 순서
# -sort, argsort

# print(np.sort(vib))     # [2.  2.1 2.3 5.8]
# print(np.argsort(vib))  # [2 0 1 3]

# 실습1
# time = col(0)
# ct = col(1)
# i = np.argmax(ct)
# shot = time[i]
# shot_time = ct[i]
# print(f'{shot}번 샷에서 사이클타임 {shot_time}초 (배열 인덱스는 {i})')

# diff
# vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
# change = np.diff(vib)
# print(np.round(change,1))
# print(np.argmax(change))

# 실습2
# data = col((0,1))
# time = data[:,0]
# ct = data[:,1]
# ct_diff = np.diff(ct)
# change = np.abs(ct_diff)
# j = np.argmax(change)
# print(f'{time[j]}번과 {time[j+1]}번 사이에서 {change[j]}초만큼 변한 것으로 출력')

# clip
# pres = np.array([4.5, 9999.0, 4.6, -1.0])
# fixed = np.clip(pres,0,10)
# print(fixed)    # -> [ 4.5 10.   4.6  0. ] 개수는 변하지 않는다

# cumsum - 누적 합
# defect = np.array([0, 1, 0, 2, 3, 5])
# print(np.cumsum(defect))

# np.where 심화
# vib = np.array([2.1, 3.5, 2.0, 6.2])
# label = np.where(vib >=5, 2, np.where(vib >= 3, 1, 0))  # 5 이상 : 2, 3 이상: 1, 나머지: 0
# print(label)

# unique - 중복 정리
# - return_counts 옵션: 각 종류의 개수 확인
# status = np.array([0,0,1,0,2,1,0])
# kinds, counts = np.unique(status, return_counts=True)
# print(kinds)
# print(counts)

# 실습3
# cyl = col(2)
# cyl[0] = 9999
# print("보정 전 평균:",np.mean(cyl).round(1))
# cor_cyl = np.clip(cyl,100,300)
# print("보정 후 평균:",np.mean(cor_cyl).round(1))

# 실습4
# ct = col(1)
# label = np.where(ct >= 1000, 2, np.where(ct>=50, 1, 0))
# kinds, counts = np.unique(label, return_counts=True)
# per = counts/ct.size
# print(f'정상 {counts[0]}, 경고 {counts[1]}, 잼 {counts[2]}, 각 비율은 {per}')

# any, all - 조건 충족 여부 판정
# - any: 하나라도 만족하면 True
# - all: 모두 만족해야 True
# vib = np.array([2.1, 3.5, 2.0, 6.2])
# print(np.any(vib>5))    # True
# print(np.all(vib<10))   # True

# # concatenate, stack - 배열 합치기
# am =np.array([2.0, 2.1, 2.2])
# pm = np.array([2.3, 2.4, 2.5])
# print(np.concatenate([am,pm]))  # [2.0  2.1 2.2 2.3 2.4 2.5]
# print(np.stack([am,pm]))    #[[2.0  2.1 2.2]
#                             #[2.3 2.4 2.5]]

# 실습5
# ct, cyp, pres, cf = col(1), col(2), col(3), col(4)
# M = np.stack([ct, cyp, pres, cf])
# print(M.shape)
# recent = M[:,-10:]
# print(recent)
# print(recent.shape)

# 실습6
time = col(0)
ct = col(1)
cyp = col(2)
print("최대 변화 시점:",time[np.argmax(ct)], "최대 변화값:",ct.max())
diff_ct = np.abs(np.diff(ct))
print("급변 시점:",time[np.argmax(diff_ct)])
caution = np.where((ct>=50) | (cyp<150),1,0)
print("경고 비율:",caution.mean())
print("변화 상위 세 시점:", time[np.argsort(ct)[::-1][:3]])