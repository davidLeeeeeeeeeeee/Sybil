import pandas as pd
from datetime import timedelta
from tqdm import tqdm
DAY = 2
df = pd.read_csv(r'filter_20group147.csv')
date_cols = ['date_1','date_4','date_7','last_date_2' ]
for col in date_cols:
    df[col] = pd.to_datetime(df[col])

grouped = df.groupby('Sybil_number')
df_filtered = pd.DataFrame()
for type_value, group in tqdm(grouped):
    is_insert = True
    for date in date_cols:
        # 计算当前组的 first_block_time 的标准差
        std = group[date].diff().std()

        if std > timedelta(days=DAY):
            is_insert = False
    if is_insert:
        df_filtered = pd.concat([df_filtered, group.reset_index(drop=True)], axis=0)

# 保存过滤后的结果为新的 CSV 文件
df_filtered.to_csv(f'Sybil_Address135_day{DAY}.csv', index=False)

df = pd.read_csv(r'filter_20group135.csv')
date_cols = ['date_1','date_3','date_5','last_date' ]
for col in date_cols:
    df[col] = pd.to_datetime(df[col])

grouped = df.groupby('Sybil_number')
df_filtered = pd.DataFrame()
for type_value, group in tqdm(grouped):
    is_insert = True
    for date in date_cols:
        # 计算当前组的 first_block_time 的标准差
        std = group[date].diff().std()

        if std > timedelta(days=DAY):
            is_insert = False
    if is_insert:
        df_filtered = pd.concat([df_filtered, group.reset_index(drop=True)], axis=0)

# 保存过滤后的结果为新的 CSV 文件
df_filtered.to_csv(f'Sybil_Address147_day{DAY}.csv', index=False)
