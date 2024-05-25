import pandas as pd

# 读取两个CSV文件
df1 = pd.read_csv('/home/liyonggang/unet_lab/Sybil_Address147_day2.csv')
df2 = pd.read_csv('/home/liyonggang/unet_lab/Sybil_Address135_day2.csv')

# 合并数据
combined_df = pd.concat([df1, df2]).drop_duplicates(subset=df1.columns[0])

# 保存合并后的数据到新的CSV文件
combined_df.to_csv('Sybil_Address_day2.csv', index=False)

print("新文件已保存，行数为：", len(combined_df))
