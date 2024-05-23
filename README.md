# Reported Addresses

`Sybil_Report_Address1.md`


## 策略
根据链上行为的高度一致性和时间一致性筛选出女巫控制地址。

具体来说，我们根据每个地址第一次（A行为）、第二次（B行为）、第三次（C行为）、最后一次（D行为）在 LayerZero 上交互合约都完全一致，并且这四次交互都在同一天以内完成，并且他们在 LayerZero 上交互的交易数量高度一致，且他们的交易金额（USD）也高度一致，并且满足这些条件的地址数量超过 20 个的，

我们可以认为他们是女巫地址。

### 原因
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
我们在dune.on_chain_behavior_consistency_analysis.sql能够L0的每个地址的所有tx数和A、B、C、D交互合约和时间选出。

后续将csv文件下载下来合并所有的csv,再依次执行deal_time.py、std_output.py、forth.py、five.py脚本。得到Sybil_Report_Address2.md文件。

## 数据解释Sybil_Report_Address1.md
| user_address                               | first_seen_date   | from                                       |   occurrence_count | source_chain   |   occurrence_count_std |
|:-------------------------------------------|:------------------|:-------------------------------------------|-------------------:|:---------------|-----------------------:|
| 0xf7e10ae6b052bc1452139043b00d49a80fa9a3d5 | 2023-02-21        | 0x192553385d46bc946a35c0870c876cee52881c08 |                 24 | arbitrum       |               3.91064  |



user_address:女巫地址。

first_seen_date：该地址的全网第一笔交易时间，即资金分发到该地址。

from：资金是来自哪个地址的。

occurrence_count：就是tx count,即该地址在LayerZero上一共发生过多少笔tx。

source_chain：该地址全网第一次是在哪个链上被激活的。

occurrence_count_std：该女巫控制的所有地址在LayerZero上tx count的标准差，用来衡量它的tx count变化波动，越小说明女巫的概率越大。

## 数据解释Sybil_Report_Address2.md
| address                                    | first_block_time          | first_destination_bridge_contract                                  | second_block_time         | second_destination_bridge_contract                                 | third_block_time          | third_destination_bridge_contract                                  | last_block_time           | last_destination_bridge_contract                                   |   tx_count |   average_amount_usd |   sybil_number |
|:-------------------------------------------|:--------------------------|:-------------------------------------------------------------------|:--------------------------|:-------------------------------------------------------------------|:--------------------------|:-------------------------------------------------------------------|:--------------------------|:-------------------------------------------------------------------|-----------:|---------------------:|---------------:|
| 0x51903df080db907d2788be785975ef72291adf68 | 2023-08-09 20:12:43+00:00 | 0x777c19834a1a2ff6353a1e9cfb7c799ed7943a11                         | 2023-08-10 22:14:46+00:00 | 0x6694340fc020c5e6b96567843da2df01b2ce1eb6                         | 2023-08-10 22:18:26+00:00 | 0xb0d502e938ed5f4df2e681fe6e419ff29631d62b                         | 2024-04-28 07:42:30+00:00 | 0xf6b88c4a86965170dd42dbb8b53e790b3490b912                         |        321 |             43.1709  |           6348 |



address:女巫地址。

first_block_time：该地址在LayerZero的第一笔tx交易时间。

first_destination_bridge_contract：该地址在LayerZero的第一笔tx的交易合约地址。

second_block_time：该地址在LayerZero的第二笔tx交易时间。

second_destination_bridge_contract：该地址在LayerZero的第二笔tx的交易合约地址。

third_block_time：该地址在LayerZero的第三笔tx交易时间。

third_destination_bridge_contract：该地址在LayerZero的第三笔tx的交易合约地址。

last_block_time：该地址在LayerZero的最后一笔tx交易时间。

last_destination_bridge_contract：该地址在LayerZero的最后一笔tx的交易合约地址。

tx_count：该地址在LayerZero上交易的tx数。

average_amount_usd：该地址在LayerZero上每笔tx的平均金额。
# Reward Address (If Eligible)
0x56646F6cEaf7C7684391B440Ac81B6Db31aBcf34
