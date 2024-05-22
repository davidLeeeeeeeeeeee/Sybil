import pandas as pd
from tqdm import tqdm
# 读取CSV文件
df = pd.read_csv('/home/liyonggang/2024-05-15-snapshot1_transactions.csv')

# 统计每个SENDER_WALLET出现的次数
sender_wallet_count = df['SENDER_WALLET'].value_counts()

# 只保留出现次数大于等于10次的SENDER_WALLET
sender_wallet_count = sender_wallet_count[sender_wallet_count >= 10]

# 过滤数据，只包含出现次数大于等于10次的SENDER_WALLET的行
df_filtered = df[df['SENDER_WALLET'].isin(sender_wallet_count.index)]

# 统计每个SENDER_WALLET的STARGATE_SWAP_USD的总和
sender_wallet_sum = df_filtered.groupby('SENDER_WALLET')['STARGATE_SWAP_USD'].sum()

# 初始化字典用于存储每个SENDER_WALLET的时间戳和目的地合约
sender_wallet_timestamps = {}

# 遍历每个SENDER_WALLET
for wallet, group in tqdm(df_filtered.groupby('SENDER_WALLET')):
    # 按照时间戳排序
    sorted_group = group.sort_values(by='SOURCE_TIMESTAMP_UTC')
    sender_wallet_timestamps[wallet] = {
        'timestamp': sorted_group['SOURCE_TIMESTAMP_UTC'].tolist(),
        'contract': sorted_group['DESTINATION_CONTRACT'].tolist()
    }

# 计算每个SENDER_WALLET的STARGATE_SWAP_USD的平均值
avg_swap_usd = sender_wallet_sum / sender_wallet_count

# 构建结果DataFrame
results = pd.DataFrame({
    'SENDER_WALLET': sender_wallet_count.index,
    'tx_count': sender_wallet_count.values,
    'avg_swap_usd': avg_swap_usd.values
})

# 获取每个SENDER_WALLET的前10笔和最后2笔交易的时间戳和合约
first_ten_timestamps = []
last_two_timestamps = []
first_ten_contracts = []
last_two_contracts = []

for wallet in tqdm(sender_wallet_timestamps, desc="Processing transactions"):
    # 获取前10笔交易时间戳和合约
    first_ten_timestamps.append(sender_wallet_timestamps[wallet]['timestamp'][:10])
    first_ten_contracts.append(sender_wallet_timestamps[wallet]['contract'][:10])

    # 获取最后2笔交易时间戳和合约
    last_two_timestamps.append(sender_wallet_timestamps[wallet]['timestamp'][-2:])
    last_two_contracts.append(sender_wallet_timestamps[wallet]['contract'][-2:])

# 将前10笔和最后2笔交易的时间戳和合约作为单独的属性列表
for i in range(10):
    results[f'first_timestamp_{i + 1}'] = [timestamps[i] if len(timestamps) > i else None for timestamps in
                                           first_ten_timestamps]

for i in range(2):
    results[f'last_timestamp_{i + 1}'] = [timestamps[i] if len(timestamps) > i else None for timestamps in
                                          last_two_timestamps]

for i in range(10):
    results[f'first_contract_{i + 1}'] = [contracts[i] if len(contracts) > i else None for contracts in
                                          first_ten_contracts]

for i in range(2):
    results[f'last_contract_{i + 1}'] = [contracts[i] if len(contracts) > i else None for contracts in
                                         last_two_contracts]

# 保存结果到CSV文件
results.to_csv('10tx_count.csv', index=False)



