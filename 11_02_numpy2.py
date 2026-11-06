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
time = col(0)
temp = col(1)
temp_mean = np.mean(temp)
temp_std = np.std(temp)
z = (temp-temp_mean)/temp_std
max_z = (temp.max()-temp_mean)/temp_std
print((time[np.abs(z) > 2]).astype(np.int64))
print(round(max_z,2))