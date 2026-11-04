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
data = []
with open("data/10_mct_tool.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row[4:])
data = np.array(data[2:6]).astype(np.float64)
print(data[2])
print("rpm:",data[:,0],"torque:",data[:,1])



