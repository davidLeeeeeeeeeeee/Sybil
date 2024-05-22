import pandas as pd

# 加载主CSV文件
df_main = pd.read_csv('10tx_count.csv')

# 加载包含要删除的地址的CSV文件
df_initial = pd.read_csv('initialList.csv')

# 在主DataFrame中删除与initialList.csv中ADDRESS字段匹配的SENDER_WALLET行
filtered_df = df_main[~df_main['SENDER_WALLET'].isin(df_initial['ADDRESS'])]

# 输出到新的CSV文件
filtered_df.to_csv('filter_del_initialList.csv', index=False)
