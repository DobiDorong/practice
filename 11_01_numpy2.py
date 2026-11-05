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
# shot = int(time[i])
# shot_time = ct[i]
# print(f'{shot}번 샷에서 사이클타임 {shot_time}초 (배열 인덱스는 {i})')

# diff
# vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
# change = np.diff(vib)
# print(np.round(change,1))
# print(np.argmax(change))

# 실습2
data = col((0,1))
time = data[:,0].astype(np.int64)
ct = data[:,1]
ct_diff = np.diff(ct)
change = np.abs(ct_diff)
j = np.argmax(change)
print(f'{time[j]}번과 {time[j+1]}번 사이에서 {change[j]}초만큼 변한 것으로 출력')
