import pandas as pd
import numpy as np
from datetime import timedelta
from tqdm import tqdm

# 定义文件路径
input_file = r'filter_20group.csv'
output_file = r'filter_time.csv'

# 读取CSV文件
df = pd.read_csv(input_file)

# 转换时间列为datetime类型
df['first_timestamp_1'] = pd.to_datetime(df['first_timestamp_1'])
df['first_timestamp_2'] = pd.to_datetime(df['first_timestamp_2'])
df['first_timestamp_3'] = pd.to_datetime(df['first_timestamp_3'])
df['first_timestamp_4'] = pd.to_datetime(df['first_timestamp_4'])
df['first_timestamp_5'] = pd.to_datetime(df['first_timestamp_5'])
df['first_timestamp_6'] = pd.to_datetime(df['first_timestamp_6'])
df['first_timestamp_7'] = pd.to_datetime(df['first_timestamp_7'])
df['first_timestamp_8'] = pd.to_datetime(df['first_timestamp_8'])
df['first_timestamp_9'] = pd.to_datetime(df['first_timestamp_9'])
df['first_timestamp_10'] = pd.to_datetime(df['first_timestamp_10'])
df['last_timestamp_1'] = pd.to_datetime(df['last_timestamp_1'])
df['last_timestamp_2'] = pd.to_datetime(df['last_timestamp_2'])

# 定义函数来控制标准差
def control_std(group, time_columns, target_std_days=1):
    target_std = timedelta(days=target_std_days).total_seconds()

    while True:
        # print(f"Removing index {group}")
        # 将时间列转换为时间戳（秒）
        timestamps = [group[col].astype('int64') // 10 ** 9 for col in time_columns]
        std_dev = np.std(timestamps, axis=1)
        if all(std <= target_std for std in std_dev):
            break

        # 找到离均值最远的元素并移除
        mean_times = {col: group[col].mean() for col in time_columns}
        furthest_index = max(
            group.index,
            key=lambda idx: max(
                abs(group.loc[idx, col].timestamp() - mean_times[col].timestamp())
                for col in time_columns
            ),
        )
        # print(f"Removing index {furthest_index}")
        group = group.drop(index=furthest_index)
        # print(f"finish Removing {furthest_index}")

    return group


# 对每个 type 进行处理并显示进度
time_columns = ['first_timestamp_1',
                'first_timestamp_2',
                'first_timestamp_3',
                'first_timestamp_4',
                'first_timestamp_5',
                'first_timestamp_6',
                'first_timestamp_7',
                'first_timestamp_8',
                'first_timestamp_9',
                'first_timestamp_10',
                'last_timestamp_1',
                'last_timestamp_2']
grouped = df.groupby('Sybil_number')

filtered_dfs = []
for name, group in tqdm(grouped, desc="Processing groups", unit="group"):
    try:
        filtered_group = control_std(group, time_columns)
        filtered_dfs.append(filtered_group)
    except Exception as e:
        print(group,e)

filtered_df = pd.concat(filtered_dfs)

# 重置索引
filtered_df.reset_index(drop=True, inplace=True)
# 删除 type 相同且行数小于20的所有 type
filtered_df = filtered_df.groupby('type').filter(lambda x: len(x) >= 20)

# 将处理后的数据保存回CSV
filtered_df.to_csv(output_file, index=False)

print(f"处理后的数据已保存到 {output_file}")
