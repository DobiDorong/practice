import numpy as np

F = 'data/11_hydraulic_cooler.csv'
def col(c) :
    return np.genfromtxt(F,delimiter=",",skip_header=1,usecols=c)


# isnan - 결측값 위치 찾기
# - 결측값: 값이 빈 칸 -> 0이 아니라 값을 모름
# x = np.array([2.0, np.nan, 4.0])
# print(np.isnan(x))  # [False  True False]
# print(np.isnan(x).sum())    # 1 (= nan 값이 몇 개인지 알 수 있다)

# # nanmean, nanstd - 결측값을 무시한 통계
# temp = np.array([70.1, np.nan, 71.2, 70.8])
# print(np.mean(temp))    # nan
# print(round(np.nanmean(temp),2))    # 70.7

# nanmean, nanmax, mammin 동일한 방식으로 사용 가능

# 실습1
# vib = col(2)
# count_nan = np.isnan(vib)
# print("결측 수: ",count_nan.sum(), "결측 비율:", np.mean(count_nan))
# print("결측 무시한 평균: ",np.nanmean(vib).round(3), "결측 포함 평균:", np.mean(vib))

# 백분위수, 사분위수 - percentile, quantile
# - 데이터를 크기순으로 줄 세웠을 때 특정 위치의 값
# - 25, 50, 75 -> 1사분위, 중앙값, 3사분위
# - 평군과 달리 극단적인 이상값에 휘둘리지 않음

# vib_s = np.array([2.0, 2.2, 2.5, 2.8, 3.0, 6.5])
# print(np.round(float(np.percentile(vib_s, 25)),2))  # 2.28
# print(np.round(float(np.percentile(vib_s, 75)),2))  # 2.65

# 여러 자리 한 번에
# print(np.round(np.percentile(vib_s,[25,50,75]),2))  # [2.28 2.65 2.95]

# quantile : 25 -> 0.25
# print(np.round(float(np.quantile(vib_s, 0.25)),2))

# # 사분위 기반 이상치 범위 - IQR
# q1, q3 = np.percentile(vib_s, [25,75])
# iqr =  q3-q1
# upper = q3 +1.5*iqr
# print(vib_s[vib_s > upper])

# 평균/표준편차로 정규화 - z-score
# - 부호의 의미: 양수는 평균보다 위, 음수는 아래
# - 방향 무시하고 크기만 보려면 절댓값 필요
# z = (vib_s - np.mean(vib_s))/np.std(vib_s)
# print(vib_s[np.abs(z) > 2])

# 실습2
# temp = col(1)
# q1,q3 = np.percentile(temp,[25,75])
# iqr = q3-q1
# upper = round(q3 + 1.5*iqr,2)
# print("상한:",upper)
# print("이상값: ",temp[temp > upper], "이상 건 수:",np.sum(temp>upper))

# 실습3
# time = col(0)
# temp = col(1)
# temp_mean = np.mean(temp)
# temp_std = np.std(temp)
# z = (temp-temp_mean)/temp_std
# print((time[np.abs(z) > 2]).astype(np.int64))
# print(round(np.abs(z).max(),2))

# 실습4
# time = col(0)
# temp = col(1)
# temp_mean, temp_std = np.mean(temp), np.std(temp)
# upper = (temp_mean + temp_std * 3).round(2)
# over = time[temp > upper].astype(int)
# print(upper, over)

# 센서 간 상관관계 - corrcoef
# - 세기는 절댓값이 정함. +0.99와 -0.99는 세기가 똑같고 방향만 반대
# - 양수: 한 쪽이 오르면 다른 한 쪽도 오름 / 음수는 반대
# - 0에 가까움 -> 관계가 없는 상태

# temp = np.array([70, 72, 74, 76, 78])
# vib = np.array([2.0, 2.2, 2.5, 2.7, 3.0])
# print(round(float(np.corrcoef(temp, vib)[0,1]),3))
# print(type((np.corrcoef(temp, vib)[0,1])))  # <class 'numpy.float64'>
# print(type(float(np.corrcoef(temp, vib)[0,1]))) # <class 'float'>
# print(np.round(np.corrcoef(temp, vib),3))
# [[1.    0.998]    온도 - 온도, 온도 - 진동
# [0.998 1.   ]]    진동 - 온도, 진동 - 진동
# 네 조합을 모두 계산해 줌

# 2D 배열 axis별 통계 활용
# 행은 센서, 열은 시점인 행렬 axis로 방향으로 정해 통계
# axis = 1 - 각 행을 옆으로 -> 센서별 통계
# axis = 0 - 각 열을 아래로 -> 시점별 통계

# data = np.array([[70., 72., 74.],[2.0, 2.2, 2.5]])
# print(np.round(np.mean(data, axis = 1),2))  # [72.    2.23]
# print(np.round(np.mean(data, axis = 0),2))  # [36.   37.1  38.25]

# 실습5
# temp = col(1)
# cool = col(3)
# print(np.round(np.corrcoef(temp, cool),3))
# print(np.round(np.corrcoef(temp, cool)[0,1],2))
# 강한 상관관계를 가지며 그 값은 반비례한다.

# 실습6
# temp, vib, cool_e, cool_p = col(1), col(2), col(3), col(4)
# data = np.stack([temp, vib, cool_e, cool_p])
# data_mean = np.nanmean(data, axis = 1).round(1)
# cor = np.round(np.nanstd(data, axis = 1),1)
# print(data_mean, cor)

# 변화점 탐지
# - 누적 합으로 찾는 원리
# - 각 값에서 전체 평균을 빼면 평균보다 작은 값은 음수, 큰 값은 양수
# - 해당 값들을 앞에서부터 누적하면 평균보다 낮은 구간에서는 계속 내려가고,
#   평균보다 높은 구간에서는 계속 올라간다.
# - 그래서 누적 곡선이 가장 낮아지는 자리가 내려가기를 멈추고 올라가기 시작한 자리

# v = np.array([2.0, 2.1, 2.0, 5.0, 5.2, 5.1])
# cs =np.cumsum(v-np.mean(v))
# print(np.argmin(cs))    # 2

# 실습7
# num, temp = col(0), col(1)
# cs = np.cumsum(temp-np.nanmean(temp))
# print(int(num[np.argmin(cs)]))

# 실습8
cy, temp, cool_e, status = col(0), col(1), col(3), col(5)
def z(a):
    return np.abs((a-np.nanmean(a)) / np.nanstd(a))
score = z(temp) + z(cool_e)

print(int(cy[np.argmax(score)]), cy[np.argsort(score)[::-1][:3]].astype(int))
print(cy[status ==1].astype(int))