import pandas as pd
from datetime import timedelta
from tqdm import tqdm
# 读取 CSV 文件
df = pd.read_csv(r'filter_20group.csv')
# 筛选出需要比较的合约字段
date_cols = [col for col in df.columns if 'timestamp' in col]
# 将日期时间列转换为 datetime 类型
for col in date_cols:
    df[col] = pd.to_datetime(df[col])

# 按 type 分组
grouped = df.groupby('Sybil_number')

# 创建一个空的 DataFrame 用于存储过滤后的数据
df_filtered = pd.DataFrame()

# 遍历每个分组
for type_value, group in tqdm(grouped):
    is_insert = True
    for date in date_cols:
        # 计算当前组的 first_block_time 的标准差
        std = group[date].diff().std()

        if std > timedelta(days=1):
            is_insert = False
    if is_insert:
        df_filtered = pd.concat([df_filtered, group.reset_index(drop=True)], axis=0)

# 保存过滤后的结果为新的 CSV 文件
df_filtered.to_csv(r'Sybil_Address.csv', index=False)

print("Filtered data saved to 'second_filter.csv'")
