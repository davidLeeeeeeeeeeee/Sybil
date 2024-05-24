# Reported Addresses

`Sybil_Address135_day1.csv`

`Sybil_Address135_day2.csv`

# Description

Identifying witch-controlled addresses based on the consistency in actions across the LayerZero network in both height and time.

Specifically, we filter out witch-controlled addresses based on the complete consistency of interactions with contracts on LayerZero for the first (Action A), third (Action B), fifth (Action C), and last (Action D) interactions, all completed within the same day. Additionally, these four interactions have highly consistent transaction counts and USD amounts, and if the number of addresses meeting these criteria exceeds 20, we consider them witch addresses.

# Detailed Methodology & Walkthrough

Our assessment is based on the following assumptions:

#### Assuming the existence of 100 different dApps on LayerZero (in reality, there are several hundred, but for simplification, let's assume 100):

<blockquote>

The probability of a completely random user having identical sequences of actions:

Probability of Action A * Probability of Action B * Probability of Action C * Probability of Action D, i.e.,

1/100 * 1/100 * 1/100 * 1/100 ≈ 0.00000001

Assuming there are 20 addresses meeting these criteria, the probability that they are regular users and not witch users is:

0.00000001^20

So the probability that they are sybil is:

** 1 - 1/100000000^20 ≈ 99.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999% **

</blockquote>

#### Considering factors like popular dApps and influencer recommendations, let's narrow down the dApp selection to 20:

<blockquote>

The probability of a completely random user having identical sequences of actions:

1/20 * 1/20 * 1/20 * 1/20 ≈ 0.00000625

Assuming there are 20 addresses meeting these criteria, the probability that they are regular users and not witch users is:

0.00000625^20

So the probability that they are sybil is:

** 1 - 0.00000625^20 ≈ 99.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999992% **

</blockquote>

This probability is still quite high.

This calculation only considers the case where contract sequences are equal. If we consider additional conditions such as tx_count, average transaction amount (USD), and the time of these actions, both probabilities will continue to increase and approach 100%.

### Method

We only used the official `2024-05-15-snapshot1_transactions.csv` database and pure Python code to select all addresses' tx counts and A, B, C, D interaction contracts and times in LayerZero.

By executing `filter_10_tx_count_01.py`, `filter_del_initialList_02.py`, `filter_20group_03.py`, `filter_day_std_04.py` in sequence, we can obtain this batch of data.

<blockquote>

1. The purpose of `filter_10_tx_count_01.py` is to filter out all data with a tx count less than 10, retain all addresses with a tx count > 10, and consolidate the times and contract addresses of the remaining addresses' first to tenth transactions.

2. The purpose of `filter_del_initialList_02.py` is to remove overlapping parts from the witch addresses published by LayerZero.

3. The purpose of `filter_20group_03.py` is to select addresses with completely identical contract addresses for the first, third, fifth, and last transactions, then perform grouping, and among the remaining data, retain the clusters with an address count greater than 20 witches.

4. The purpose of `filter_day_std_04.py` is to select addresses where the execution times of these A, B, C, D actions (within the same day or two days) are highly consistent. This means not only are the contract addresses identical but also the execution times are consistent. The files `Sybil_Address135_day1.csv` and `Sybil_Address135_day2.csv` are set for 1 day and 2 days, respectively.

</blockquote>

After layers of filtering, we found that the remaining addresses also have a high consistency in tx_count, avg_swap_usd, and LZ_Age_In_Days, so we conclude that they are definitely witch addresses.

## Data Explanation for Sybil_Address135_day1.csv
| SENDER_WALLET | tx_count | avg_swap_usd | Sybil_number | LZ_Age_In_Days | Activate_Date | date_1 | date_2 | date_3 | date_4 | date_5 | date_6 | date_7 | date_8 | date_9 | date_10 | last_date | last_date_2 | action_1 | action_2 | action_3 | action_4 | action_5 | action_6 | action_7 | action_8 | action_9 | action_10 | last_contract | last_contract_2 | contract_tuple |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0xa55d2cb234898724c2a5932663a7f9749bd92382 | 17 | 97.98357055611766 | 24 | 9 | 2024-01-31 | 2024-01-31 | 2024-02-25 | 2024-03-24 | 2024-04-19 | 2024-04-19 | 2024-04-20 | 2024-04-20 | 2024-04-20 | 2024-04-21 | 2024-04-24 | 2024-04-28 | 2024-04-28 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0xa4218e1f39da4aadac971066458db56e901bcbde+0x29d096cd18c0da7500295f082da73316d704031a | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x79f3649d8084ea76f91700eefc3bc1493fb3d731 | 17 | 91.60472793264704 | 24 | 9 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-24 | 2024-04-19 | 2024-04-19 | 2024-04-19 | 2024-04-20 | 2024-04-21 | 2024-04-22 | 2024-04-24 | 2024-04-28 | 2024-04-28 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x59781ead62035616f9c4852dead0dacbe3b84f33 | 17 | 95.930526926 | 24 | 10 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-24 | 2024-04-19 | 2024-04-19 | 2024-04-19 | 2024-04-20 | 2024-04-21 | 2024-04-22 | 2024-04-23 | 2024-04-28 | 2024-04-28 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x123450714b677b1ae24dc28959c7e833159e4321+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x529ed86ad8f1b47a7482a492e0d82fe1f7c0b886 | 17 | 98.09099831394116 | 24 | 9 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-25 | 2024-04-19 | 2024-04-19 | 2024-04-19 | 2024-04-20 | 2024-04-21 | 2024-04-21 | 2024-04-23 | 2024-04-28 | 2024-04-28 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0xa4218e1f39da4aadac971066458db56e901bcbde+0x29d096cd18c0da7500295f082da73316d704031a | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x3431e1d987d442074e0138baf60c84e228f72c42 | 17 | 97.48251620964706 | 24 | 10 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-25 | 2024-04-20 | 2024-04-20 | 2024-04-20 | 2024-04-22 | 2024-04-24 | 2024-04-25 | 2024-04-26 | 2024-04-29 | 2024-04-29 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0xa4218e1f39da4aadac971066458db56e901bcbde+0x29d096cd18c0da7500295f082da73316d704031a | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x3e65d0a2f2541a2558b9852a2b9f697791f136ed | 17 | 94.61222562688236 | 24 | 8 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-25 | 2024-04-21 | 2024-04-21 | 2024-04-21 | 2024-04-21 | 2024-04-24 | 2024-04-24 | 2024-04-25 | 2024-05-01 | 2024-05-01 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0x042002711e4d7a7fc486742a85dbf096beeb0420+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x123450714b677b1ae24dc28959c7e833159e4321+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0xa4218e1f39da4aadac971066458db56e901bcbde+0x29d096cd18c0da7500295f082da73316d704031a | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |
| 0x72161da918b89602e71d9eeb759a7d78017ebdd5 | 17 | 98.23553773994117 | 24 | 8 | 2024-01-31 | 2024-01-31 | 2024-02-24 | 2024-03-24 | 2024-04-21 | 2024-04-21 | 2024-04-21 | 2024-04-21 | 2024-04-24 | 2024-04-24 | 2024-04-26 | 2024-04-30 | 2024-04-30 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |




- SENDER_WALLET: Witch address.

- tx_count: The number of transactions the address has on LayerZero.

- avg_swap_usd: The average swap funds per transaction of the address on LayerZero.

- Sybil_number: Witch number, same witch number indicates the same cluster.

- LZ_Age_In_Days: The active days of the address on LayerZero.

- date_1~date_10: The occurrence time of the first to tenth transactions of the address on LayerZero.

- last_date: The transaction time of the last transaction of the address on LayerZero.

- last_date_2: The transaction time of the second-to-last transaction of the address on LayerZero.

- last_block_time: The transaction time of the last transaction of the address on LayerZero.

- action_1~action_10: The contract addresses (DESTINATION_CONTRACT+SOURCE_CONTRACT) of the first to tenth transactions of the address on LayerZero.

- last_contract: The contract address of the last transaction of the address on LayerZero.

- last_contract_2: The contract address of the second-to-last transaction of the address on LayerZero.

- contract_tuple: The tuple of all the above addresses.

- average_amount_usd: The average amount per transaction of the address on LayerZero.

# Reward Address (If Eligible)
0x56646F6cEaf7C7684391B440Ac81B6Db31aBcf34
