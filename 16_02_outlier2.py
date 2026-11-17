import pandas as pd

FD = 'data/16_diecasting.csv'
FW = 'data/16_welding.csv'

df = pd.read_csv(FD)
df_w = pd.read_csv(FW)

# Q1 = df["사이클타임"].quantile(0.25)
# Q3 = df["사이클타임"].quantile(0.75)
# IQR = Q3-Q1
# lower = Q1 - IQR*1.5
# upper = Q3 + IQR*1.5

# ct_clipped = df['사이클타임'].clip(lower= lower, upper=upper)
# print(round(ct_clipped.min(),2), round(ct_clipped.max(),2),
#       round(ct_clipped.mean(),2))

# 실습1
Q1 = df["사이클타임"].quantile(0.25)
Q3 = df["사이클타임"].quantile(0.75)
IQR = (Q3-Q1).round(2)
lower = round(Q1 - IQR*1.5,2)
upper = round(Q3 + IQR*1.5,2)
print(IQR, lower, upper)