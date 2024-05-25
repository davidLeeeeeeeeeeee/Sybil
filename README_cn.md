# Reported Addresses

`Sybil_Address_day1.csv`

`Sybil_Address_day2.csv`

# Description
根据链上行为的高度一致性和时间一致性筛选出女巫控制地址。


具体来说，我们根据每个地址第一次（A transaction）、第三次（B transaction）、第五次（C transaction）、最后一次（D transaction）在 LayerZero 上交互合约都完全一致，并且这四次交互都在同一天以内完成。尽管我们筛选条件只有合约地址、时间，但是我们却发现他们的tx count、平均交易金额（USD）、unique active day也高度一致。除了上述的时间和合约地址的条件，我们还设置了同一簇地址数量超过 20 个的，
才是Sybil地址。


e.g. 假设有2个地址他们的第一次交易都是同一合约且同一天执行，就认为A transaction满足条件。同时当这两个地址B、C、D transaction也都满足的时候，就认为这两个地址受同一Sybil控制。

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
我们仅仅使用了官方提供的`2024-05-15-snapshot1_transactions.csv`数据库，用纯python代码，能够L0的每个地址的所有tx数和A、B、C、D交互合约和时间选出。

只需要依此执行`filter_10_tx_count_01.py`、`filter_del_initialList_02.py`、`filter_20group_03.py`、`filter_day_std_04.py`、就能够得到这批数据。

<blockquote>
  
1.  `filter_10_tx_count_01.py`的作用是筛掉tx count小于10的所有数据，保留tx count > 10的所有address,再把剩下的address的1~10笔交易的时间和合约地址归拢到一起。

2.  `filter_del_initialList_02.py`的作用是从LayerZero官方公布的女巫地址中，筛掉重叠的部分。

3.  `filter_20group_03.py`的作用是选出第一笔，第三笔，第五笔，最后一笔合约地址完全相同的adress然后group操作，并且在剩下的数据中，保留address count 大于20个的巫女簇。

4.  `filter_day_std_04.py`的作用是选出这A、B、C、D四个action的执行时间(同一天或两天)都高度一致的address，这意味着不仅合约地址一致，连执行的时间都是一致的。上面提到的 `Sybil_Address_day1.csv` 就是设置为DAY=1, `Sybil_Address_day2.csv` 就是设置为DAY=2,如果您想复现我的结果，只需要改这一个参数（'DAY'）就能复现成功.
   

</blockquote>
经过层层筛选，我们发现保留下来的地址还具备tx_count , avg_swap_usd, LZ_Age_In_Days的高度一致性，所以我们断定他们绝对是女巫地址。

## 数据解释Sybil_Address_day1.csv
<img src="https://i.imgur.com/EWvKUMZ.png">



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

  
# Reward Address (If Eligible)
0x56646F6cEaf7C7684391B440Ac81B6Db31aBcf34
