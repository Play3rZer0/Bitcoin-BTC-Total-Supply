# Bitcoin-BTC-Calculator
These programs compute the total Bitcoin reward sizes, and the actual total supply of bitcoins.

The purpose of this project is to calculate the actual total supply of Bitcoin, which many assume is 21 million bitcoins.
That is actually not the exact number, and that requires some explanation.

1. Bitcoin does not use decimals in division, it uses integer math.
2. Bitcoin software protocol uses bitshift-operators.

Bitcoin's actual total supply is 20,999,999.9769 BTC, or 2,310,000 satoshis short of 21 million. 
This can be an interesting topic to discuss in Bitcoin and crypto circles.

Bitcoin truncates decimals when halving block rewards due to the way the reward schedule is defined within its protocol. That 
is why in explanation #1 decimals in division are discarded or truncated. The protocol will round the number to the nearest
whole integer value.

I present two programs in this project that are written in Python (version 3.6.5 and higher).

TotalRewardSize.py : This computes the total reward sizes only, not the total rewards issued (BTC created). This is taken from
each of the halving events, of which there are 32 significant halvings. Beyond that the protocol will continue the halving
process, but rewards will be insignificant to miners because they are at 0. The sum of all reward sizes from each halving totals to 
approximately 100 BTC/halving blocks. When multiplied with the 210,000 halving blocks in each halving process. This is how you
get the popular or more well known information that Bitcoin's total supply is 21,000,000 BTC.

TotalBitcoinSupply.py: 
  


