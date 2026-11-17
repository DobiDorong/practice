import pandas as pd

FD = 'data/16_diecasting.csv'
FW = 'data/16_welding.csv'

df = pd.read_csv(FD)
df_w = pd.read_csv(FW)

# 실습1
# df = pd.read_csv(FD)
# print(df.head())
# print(df.shape, df.columns.tolist())
# print(df.info())

# 실습2
# cy_max = int(df["실린더압력"].max())
# cy_min = int(df["실린더압력"].min())
# cy_gap = cy_max - cy_min
# print(cy_max, cy_min, cy_gap)

# 실습3
# sorted_time = df["사이클타임"].sort_values(ascending=False)
# print(sorted_time)
# big = sorted_time.head(1)
# print(big)

# 실습4
# cy_mean = df['사이클타임'].mean()
# cy_median = df['사이클타임'].median()
# print(cy_median, cy_mean)
# stan = df[(df['사이클타임'] >= 20) & (df['사이클타임'] <= 40)]
# print(stan["사이클타임"].mean().round(2))

# 실습5
# cy = df["실린더압력"]
# print(cy.quantile(0.25))
# print(cy.quantile(0.50))
# print(cy.median())
# print(cy.quantile(0.75))

# 실습6
# print(df.describe())
# df_mean = df.mean()
# df_medi = df.median()
# print((df_mean - df_medi).abs().sort_values(ascending=False))

# 실습7
d = df[["실린더압력","사이클타임","비스킷두께"]]
d_q3 = d.quantile(0.75)
d_q1 = d.quantile(0.25)
gap =d_q3 - d_q1
print(gap)