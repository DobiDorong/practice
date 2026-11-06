import numpy as np
import os
import csv

# 인덱싱, 슬라이싱
# a = np.arange(5)
# print(a[0],a[-1])   # 0 4
# print(a[1:4])
# print(a[:])
# print(a[::2])
# print(a[:-1])
# 2차원 인덱싱 행: a[행 번호], 열: a[:,열 번호], 특정 위치 a[행 번호, 열 번호]

# 실습 1
# rpm = []
# with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         rpm.append(row[4])
# rpm = np.array(rpm[1:11])
# print(rpm)
# print(rpm[0], rpm[-1])
# print(rpm[3:5])
# print(rpm[::2])

# 실습2
# data = []
# with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         data.append(row[4:])
# data = np.array(data[2:6]).astype(np.float64)
# print(data[2])
# print("rpm:",data[:,0],"torque:",data[:,1])

# # 배열 산술 연산
# a = np.array([1,2,3])
# b = np.array([10,20,30])
# print(a+b)
# print(b*1.8+32)     # 숫자 하나는 각 칸에 적용

# # 브로드캐스팅
# table =np.array([[72,2.3],[95,6.8]])
# base = np.array([70,2.0])
# print(table-base)   # 각 행에서 기준값 빼기
# 칸의 크기가 맞지 않으면 안됨

# 실습3
# rpm = []
# with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         rpm.append(row[4])
# rpm = np.array(rpm[1:11]).astype(np.float64)
# print(max(rpm),min(rpm))
# rpm_1 = rpm-min(rpm)
# rpm_2 = rpm_1 /(max(rpm)-min(rpm))
# print(rpm_1,rpm_2.round(2))

# 비교 연산과 불리언 배열
# vals = np.array([70,95,71,88,73])
# print(vals>75)      # [False  True False  True False]

# 불리언 인덱싱
# - 조건이 참/거직인 배열을 만듦 -> 그 배열을 대괄호에 넣으면 참인 값만 남는다
# print(vals[vals > 75])      #[95 88]

# np.where(조건, 참일 때 값, 거짓일 때 값)
# print(np.where(vals > 85, 1, 0))    #[0 1 0 1 0]

# 다중 조건
# print(vals[(vals > 70) & (vals<90)])    #[71 88 73]

# 실습4
# rpm = []
# current = []
# with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         rpm.append(float(row[4]))
#         current.append(float(row[3]))
# rpm = np.array(rpm)
# current = np.array(current)
# cond1 = rpm < 4000
# cond2 = (rpm < 4000) | (current > 25)
# print(cond1)
# print(cond2)
# print(np.sum(cond1),np.sum(cond2))
# print(np.mean(cond1)*100)
# print(np.mean(cond2)*100)

# 실습5
# torque = []
# with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)
#     for row in reader:
#         torque.append(float(row[5]))
# torque = np.array(torque[0:10])
# torque_bul = torque > 10
# print(np.sum(torque_bul))
# print(np.mean(torque_bul))

# 통계
# - 정상을 알아야 이상을 알 수 있다
# ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판다 가능
# - 평균, 최대/최소, 표준편차, 분산
# - Numpy에서 함수 하나로 계산

# s = np.array([70, 72, 71, 95, 73])
# print("합계:", s.sum())
# print("평균:", s.mean())
# print("합계:", np.median(s))
# print("최대:", s.max())
# print("최소:", s.min())

# # 분산
# stable = np.array([70,71,70,72,71])
# unstable = np.array([60,85,65,95,70])
# print(round(stable.var(),1))    # 0.6
# print(round(unstable.var(),1))  # 170.0

# 표준편차
# print(round(stable.std(),2))    # 0.75
# print(round(unstable.std(),2))  # 13.04

# axis 개념 (행/열 방향)
# mat = np.array([[70,2.1],[72,2.3]])
# print(mat.mean(axis=0))     # 열별 평균 (센서별)
# print(mat.mean(axis=1))     # 행별 평균 (시점별) -> 지금은 큰 의미 X
# print(mat.mean())           # 전체 평균

# 실습6
data = []
with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        data.append(row[4:])
data = np.array(data).astype(np.float64)
# print(data)
print(data.mean(axis = 0).round(1))
print(data.std(axis=0).round(1))

# 파일에서 배열로 불러오기(np.loadtxt)

# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",      # 값을 나누는 기호
#                  skiprows=1,        # 첫 줄(제목)은 건너뜀
#                  usecols=4)         # 5번째 열 = 회전수
# print(rpm)

# data_rt = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",      # 값을 나누는 기호
#                  skiprows=1,        # 첫 줄(제목)은 건너뜀
#                  usecols=(4,5))         # 5번째 열 = 회전수
# print(data_rt)

# 실습7
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",    
#                  skiprows=1,       
#                  usecols=4)
# avg_rpm = round(rpm.mean(),1)
# var_rpm = round(rpm.std(),1)
# max_rpm = rpm.max()
# min_rpm = rpm.min()

# print(avg_rpm, var_rpm, max_rpm, min_rpm)

# 실습8
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",    
#                  skiprows=1,       
#                  usecols=5)
# rpm_over = rpm[rpm > 10]
# print(rpm_over)
# print("개수:",rpm_over.size,"평균:",rpm_over.mean())
# print("전체 평균:",rpm.mean(),"평균 차이:", rpm.mean()-rpm_over.mean())

# 실습9
rpm = np.loadtxt('data/10_mct_tool.csv',
                 delimiter=",",    
                 skiprows=1,       
                 usecols=(4,5))
print(rpm.shape)
print(rpm.dtype)
col_rpm = rpm[:,0]
rpm_under = col_rpm[col_rpm < 2000]
print("이상 시점:",rpm_under.size,"이상 평균:",rpm_under.mean(),
        "전체 평균:",col_rpm.mean())
