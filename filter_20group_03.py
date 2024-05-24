import pandas as pd

# 加载CSV数据
df = pd.read_csv('filter_del_initialList.csv')

# 筛选出需要比较的合约字段
# contract_cols = [col for col in df.columns if 'contract' in col]
contract_cols = ['action_1','action_3','action_5','last_contract' ]
# 创建一个新列，将所有合约字段合并成一个元组，用于后续比较
df['contract_tuple'] = df.apply(lambda row: tuple(row[col] for col in contract_cols), axis=1)

# 分组并计数，只保留计数大于等于20的组
grouped = df.groupby('contract_tuple').filter(lambda x: len(x) >= 20)

# 为这些组分配唯一的Sybil_number，并指定索引位置为第4列
grouped.insert(3, 'Sybil_number', grouped['contract_tuple'].rank(method='dense').astype(int))

# 按Sybil_number排序
final_df = grouped.sort_values(by='Sybil_number')

# 输出到新的CSV文件
final_df.to_csv('filter_20group.csv', index=False)
