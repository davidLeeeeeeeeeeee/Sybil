# Reported Addresses

`Sybil_Address135_day1.csv`
`Sybil_Address135_day2.csv`
# Description
根据链上行为的高度一致性和时间一致性筛选出女巫控制地址。

具体来说，我们根据每个地址第一次（A行为）、第三次（B行为）、第五次（C行为）、最后一次（D行为）在 LayerZero 上交互合约都完全一致，并且这四次交互都在同一天以内完成，并且他们在 LayerZero 上交互的交易数量高度一致，且他们的交易金额（USD）也高度一致，并且满足这些条件的地址数量超过 20 个的，

我们可以认为他们是女巫地址。

# Detailed Methodology & Walkthrough
我们这么做的判断依据是
#### 假设 LayerZero 上存在 100 个不同的 dApp（实际上有好几百个，为了简化计算这里假设100个）：
<blockquote>



那么完全随机用户他们四个顺序上操作完全一致的概率是：

A行为概率 * B行为概率 * C行为概率 * D行为概率  即：

1&frasl;100 * 1&frasl;100 * 1&frasl;100 * 1&frasl;100 ≈ 0.00000001

假设有 20 个号都是满足这些条件，他们是普通用户，而不是女巫用户的概率是：

0.00000001<sup>20</sup>

所以他们是女巫的概率则是：

1 - 1&frasl;100000000<sup>20</sup> ≈ 99.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999%


</blockquote>

#### 考虑到可能有热门dapp和大V推荐等因素，我不妨把dapp选择范围缩小到20个：

<blockquote>
那么随机用户的操作顺序完全一致的概率：
1&frasl;20 * 1&frasl;20 * 1&frasl;20 * 1&frasl;20 ≈ 0.00000625

假设有 20 个号都是满足这些条件，他们是普通用户，而不是女巫用户的概率是：

0.00000625<sup>20</sup>

所以他们是女巫的概率则是：

1 - 0.00000625<sup>20</sup> ≈ 99.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999992%

这个概率依然是相当夸张的高。
</blockquote>

这还仅仅计算了合约顺序相等的情况，如果考虑到tx_count、平均交易金额（USD）、这些行为发生的时间等条件,那么这两个概率都会持续增加而接近 100%。

### 方法
我们仅仅使用了官方提供的2024-05-15-snapshot1_transactions.csv数据库，用纯python代码，能够L0的每个地址的所有tx数和A、B、C、D交互合约和时间选出。

只需要依此执行`filter_10_tx_count_01.py`、`filter_del_initialList_02.py`、`filter_20group_03.py`、`filter_day_std_04.py`、就能够得到这批数据。

1.  `filter_10_tx_count_01.py`的作用是筛掉tx count小于10的所有数据，保留tx count > 10的所有address,再把剩下的address的1~10笔交易的时间和合约地址归拢到一起。

2.  `filter_del_initialList_02.py`的作用是从LayerZero官方公布的女巫地址中，筛掉重叠的部分。

3.  `filter_20group_03.py`的作用是选出第一笔，第三笔，第五笔，最后一笔合约地址完全相同的adress然后group操作，并且在剩下的数据中，保留address count 大于20个的巫女簇。

4.  `filter_day_std_04.py`的作用是选出这A、B、C、D四个action的执行时间(同一天或两天)都高度一致的address，这意味着不仅合约地址一致，连执行的时间都是一致的。

经过层层筛选，我们发现保留下来的地址还具备tx_count , avg_swap_usd, LZ_Age_In_Days的高度一致性，所以我们断定他们绝对是女巫地址。

## 数据解释Sybil_Address135_day1.csv
| SENDER_WALLET | tx_count | avg_swap_usd | Sybil_number | LZ_Age_In_Days | Activate_Date | date_1 | date_2 | date_3 | date_4 | date_5 | date_6 | date_7 | date_8 | date_9 | date_10 | last_date | last_date_2 | action_1 | action_2 | action_3 | action_4 | action_5 | action_6 | action_7 | action_8 | action_9 | action_10 | last_contract | last_contract_2 | contract_tuple |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0xa55d2cb234898724c2a5932663a7f9749bd92382 | 17 | 97.98357055611766 | 24 | 9 | 2024-01-31 | 2024-01-31 | 2024-02-25 | 2024-03-24 | 2024-04-19 | 2024-04-19 | 2024-04-20 | 2024-04-20 | 2024-04-20 | 2024-04-21 | 2024-04-24 | 2024-04-28 | 2024-04-28 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd+0x701a95707a0290ac8b90b3719e8ee5b210360883 | 0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x042002711e4d7a7fc486742a85dbf096beeb0420 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x701a95707a0290ac8b90b3719e8ee5b210360883+0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398 | 0x222228060e7efbb1d78bb5d454581910e3922222+0x222228060e7efbb1d78bb5d454581910e3922222 | 0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222 | 0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde | 0xa4218e1f39da4aadac971066458db56e901bcbde+0x29d096cd18c0da7500295f082da73316d704031a | ('0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0x0000049f63ef0d60abe49fdd8bebfa5a68822222+0x0000049f63ef0d60abe49fdd8bebfa5a68822222', '0xaf54be5b6eec24d6bfacf1cce4eaf680a8239398+0x352d8275aae3e0c2404d9f68f6cee084b5beb3dd', '0x29d096cd18c0da7500295f082da73316d704031a+0xa4218e1f39da4aadac971066458db56e901bcbde') |




- SENDER_WALLET:女巫地址。

- tx_count：该地址在LayerZero上交易的tx数。

- avg_swap_usd：该地址在LayerZero的每笔tx的平均swap资金。

- Sybil_number：女巫编号，同样的女巫编号为同一簇。

- LZ_Age_In_Days：该地址在LayerZero的活跃天数。

- date_1~date_10：该地址在LayerZero的第一笔到第十笔tx的发生时刻。

- last_date：该地址在LayerZero的最后一笔tx交易时间。

- last_date_2：该地址在LayerZero的倒数第二笔tx的交易合约地址。

- last_block_time：该地址在LayerZero的最后一笔tx交易时间。

- action_1~action_10：该地址在LayerZero的第一笔到第十笔tx的合约地址（DESTINATION_CONTRACT+SOURCE_CONTRACT）。

- last_contract：该地址在LayerZero的最后一笔tx的合约地址。

- last_contract_2： 该地址在LayerZero的倒数第二笔tx的合约地址。

- contract_tuple： 上面所有地址的元组。

- average_amount_usd：该地址在LayerZero上每笔tx的平均金额。
  
# Reward Address (If Eligible)
0x56646F6cEaf7C7684391B440Ac81B6Db31aBcf34
