import pandas as pd
from tqdm import tqdm
# 读取CSV文件
df = pd.read_csv('./2024-05-15-snapshot1_transactions.csv')

# 统计每个SENDER_WALLET出现的次数
sender_wallet_count = df['SENDER_WALLET'].value_counts()

# 只保留出现次数大于等于10次的SENDER_WALLET
sender_wallet_count = sender_wallet_count[sender_wallet_count >= 10]

# 过滤数据，只包含出现次数大于等于10次的SENDER_WALLET的行
df_filtered = df[df['SENDER_WALLET'].isin(sender_wallet_count.index)]

# 统计每个SENDER_WALLET的STARGATE_SWAP_USD的总和
sender_wallet_sum = df_filtered.groupby('SENDER_WALLET')['STARGATE_SWAP_USD'].sum()

# Convert 'SOURCE_TIMESTAMP_UTC' to datetime
df_filtered['SOURCE_TIMESTAMP_UTC'] = pd.to_datetime(df_filtered['SOURCE_TIMESTAMP_UTC']).dt.date
groupby_pd = df_filtered.groupby('SENDER_WALLET')
# Group by 'SENDER_WALLET' and count unique 'SOURCE_TIMESTAMP_UTC'
result_day = groupby_pd['SOURCE_TIMESTAMP_UTC'].nunique()

# 初始化字典用于存储每个SENDER_WALLET的时间戳和目的地合约
sender_wallet_timestamps = {}

# 遍历每个SENDER_WALLET
for wallet, group in tqdm(groupby_pd):
    # 按照时间戳排序 SOURCE_CONTRACT
    sorted_group = group.sort_values(by='SOURCE_TIMESTAMP_UTC')
    timestamps = sorted_group['SOURCE_TIMESTAMP_UTC'].tolist()
    top_contracts = sorted_group['DESTINATION_CONTRACT'].tolist()
    top_source = sorted_group['SOURCE_CONTRACT'].tolist()
    sender_wallet_timestamps[wallet] = {
        'Activate_Date': timestamps[0],
        'date_1': timestamps[0],
        'date_2': timestamps[1],
        'date_3': timestamps[2],
        'date_4': timestamps[3],
        'date_5': timestamps[4],
        'date_6': timestamps[5],
        'date_7': timestamps[6],
        'date_8': timestamps[7],
        'date_9': timestamps[8],
        'date_10': timestamps[9],
        'last_date': timestamps[-1],
        'last_date_2': timestamps[-2],
        'action_1': top_contracts[0]+ '+' + top_source[0],
        'action_2': top_contracts[1]+ '+' + top_source[1],
        'action_3': top_contracts[2]+ '+' + top_source[2],
        'action_4': top_contracts[3]+ '+' + top_source[3],
        'action_5': top_contracts[4]+ '+' + top_source[4],
        'action_6': top_contracts[5]+ '+' + top_source[5],
        'action_7': top_contracts[6]+ '+' + top_source[6],
        'action_8': top_contracts[7]+ '+' + top_source[7],
        'action_9': top_contracts[8]+ '+' + top_source[8],
        'action_10': top_contracts[9]+ '+' + top_source[9],
        'last_contract': top_contracts[-1]+ '+' + top_source[-1],
        'last_contract_2': top_contracts[-2]+ '+' + top_source[-2],
    }

# 计算每个SENDER_WALLET的STARGATE_SWAP_USD的平均值
avg_swap_usd = sender_wallet_sum / sender_wallet_count

# 将每个 Series 转换为 DataFrame，并指定列名
sender_wallet_count_df = pd.DataFrame({'SENDER_WALLET': sender_wallet_count.index, 'tx_count': sender_wallet_count.values}, index=sender_wallet_count.index)
avg_swap_usd_df = pd.DataFrame({'avg_swap_usd': avg_swap_usd.values}, index=avg_swap_usd.index)
result_day_df = pd.DataFrame({'LZ_Age_In_Days': result_day.values}, index=result_day.index)

# 使用 concat() 函数将它们按列合并为一个 DataFrame
results = pd.concat([sender_wallet_count_df, avg_swap_usd_df, result_day_df], axis=1)

# 使用 map 函数将字典中的值映射到新列
results['Activate_Date'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['Activate_Date'])
results['date_1'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_1'])
results['date_2'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_2'])
results['date_3'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_3'])
results['date_4'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_4'])
results['date_5'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_5'])
results['date_6'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_6'])
results['date_7'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_7'])
results['date_8'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_8'])
results['date_9'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_9'])
results['date_10'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['date_10'])
results['last_date'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['last_date'])
results['last_date_2'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['last_date_2'])
results['action_1'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_1'])
results['action_2'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_2'])
results['action_3'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_3'])
results['action_4'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_4'])
results['action_5'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_5'])
results['action_6'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_6'])
results['action_7'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_7'])
results['action_8'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_8'])
results['action_9'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_9'])
results['action_10'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['action_10'])
results['last_contract'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['last_contract'])
results['last_contract_2'] = results['SENDER_WALLET'].map(lambda x: sender_wallet_timestamps[x]['last_contract_2'])
# 保存结果到CSV文件
results.to_csv('10tx_count.csv', index=False)


