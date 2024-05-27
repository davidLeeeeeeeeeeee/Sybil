# Reported Addresses

`Sybil_Address_day1.csv` 215 clusters
https://drive.google.com/file/d/17ft_bcUpRruyqll9tGvpjZUslQp_8BxK/view?usp=drive_link
`Sybil_Address_day2.csv` 402 clusters
https://drive.google.com/file/d/1ayFfrsrF-ZSIyNQ8OIwSEoJhFphbEZmc/view?usp=drive_link
# Description
Sybil-controlled addresses are identified based on the high consistency of on-chain behavior and timing.


Specifically, we select addresses where their first (A transaction), third (B transaction), fifth (C transaction), and last (D transaction) interactions on LayerZero are identical, and all four interactions are completed within the same day. Although our selection criteria are limited to contract address and time, we found their tx count, average transaction amount (USD), and unique active day are also highly consistent. Besides the aforementioned time and contract address criteria, we also set a condition that there must be more than 20 addresses in the same cluster to be classified as Sybil addresses.


e.g., If two addresses have their first transaction on the same contract and the same day, it's considered that the A transaction meets the criteria. If their B, C, and D transactions also meet the conditions, then these two addresses are considered to be controlled by the same Sybil.

# Detailed Methodology & Walkthrough
Our reasoning is based on the assumption that:
#### Assuming there are 100 different dApps on LayerZero (actually several hundred, but let's simplify to 100):
<blockquote>

The probability that four sequential actions by completely random users are identical is:

Probability of A * Probability of B * Probability of C * Probability of D, which is:

1/100 * 1/100 * 1/100 * 1/100 ≈ 0.00000001

If there are 20 accounts that meet these criteria, and they are ordinary users, not Sybil users, their probability is:

0.00000001<sup>20</sup>

Thus, the probability they are Sybil-controlled is:

**1 - 1/100000000<sup>20</sup> ≈ 99.99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999%**

</blockquote>

#### Considering factors like popular dApps and endorsements by influencers, let's reduce the range of dApp choices to 20:

<blockquote>

The probability that the sequence of actions by random users is identical:

1/20 * 1/20 * 1/20 * 1/20 ≈ 0.00000625

If there are 20 accounts that meet these criteria, and they are ordinary users, not Sybil users, their probability is:

0.00000625<sup>20</sup>

Thus, the probability they are Sybil-controlled is:

**1 - 0.00000625<sup>20</sup> ≈ 99.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999992%**

This probability is still extraordinarily high.
</blockquote>

This calculation only considers the case where the contract sequence is equal. If we consider additional conditions like tx_count, average transaction amount (USD), and the timing of these actions, both probabilities will increase and approach 100%.

#### Data Source

We only used the official `2024-05-15-snapshot1_transactions.csv` database.

#### Method

##### Quick Start

```python

git clone https://github.com/davidLeeeeeeeeeeee/Sybil.git

cd Sybil

pip install -r requirements.txt

```

With pure Python code, it's possible to select Sybil addresses in L0's transaction data for each address where the contract and timing of interactions A, B, C, and D meet the conditions.

You just need to execute `filter_10_tx_count_01.py`, `filter_del_initialList_02.py`, `filter_20group_03.py`, `filter_day_std_04.py` in sequence to obtain this batch of data.

<blockquote>
  
step 1.  

```python

python filter_10_tx_count_01.py

```
**This command filters out all data with tx count less than 10, retaining all addresses with tx count > 10, and groups the contract addresses and timing of the first 10 transactions of the remaining addresses together.**

step 2.

```python

python filter_del_initialList_02.py

```

**This command filters out the overlapping parts from the Sybil addresses officially announced by LayerZero, eliminating duplicates.**

step 3.

```python

python filter_20group_03.py

```
**This command selects addresses where the contract addresses of the first, third, fifth, and last transactions are identical, then groups them, and retains clusters where the count of addresses exceeds 20.**

step 4.

```python

python filter_day_std_04.py

```
**This command selects addresses where the execution timing of actions A, B, C, and D (same day or two days) is highly consistent, indicating not only identical contract addresses but also consistent execution timing. The mentioned Sybil_Address_day1.csv sets DAY=1, and Sybil_Address_day2.csv sets DAY=2. If you want to replicate my results, you only need to change this parameter ('DAY') to succeed.**

</blockquote>

**After layers of filtering, we found that the retained addresses also exhibit high consistency in tx_count, avg_swap_usd, and LZ_Age_In_Days, thus we are confident they are Sybil addresses.**

## Data Display for Sybil_Address_day1.csv

<img src="https://i.imgur.com/DOkTOVb.png">
<img src="https://i.imgur.com/isYfOMR.png">
<img src="https://i.imgur.com/5MIwRqx.png">

### Visual Analysis

From the tables, we can clearly see that although our selection criteria include only the 1st, 3rd, 5th, and last transactions, these Sybil addresses maintain a high degree of consistency in tx count, average swap usd, independent active days, and even other actions' time and addresses.

### Parameter Explanation

- SENDER_WALLET: Sybil address.

- tx_count: Number of transactions this address has on LayerZero.

- avg_swap_usd: Average swap amount in USD per transaction for this address on LayerZero.

- Sybil_number: Sybil number, the same number indicates the same cluster.

- LZ_Age_In_Days: Active days of this address on LayerZero.

- date_1~date_10: The moments of the first to tenth transactions of this address on LayerZero.

- last_date: The transaction time of the last transaction of this address on LayerZero.

- last_date_2: Contract address of the penultimate transaction of this address on LayerZero.

- last_block_time: Transaction time of the last transaction of this address on LayerZero.

- action_1~action_10: Contract addresses of the first to tenth transactions of this address on LayerZero (DESTINATION_CONTRACT+SOURCE_CONTRACT).

- last_contract: Contract address of the last transaction of this address on LayerZero.

- last_contract_2: Contract address of the penultimate transaction of this address on LayerZero.

  # Reward Address (If Eligible)

    0x6062aaB07A11DfAd6e2BF48C11Bedd62853363dF
