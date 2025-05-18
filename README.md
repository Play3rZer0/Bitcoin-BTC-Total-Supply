## Bitcoin-BTC-Total-Supply-Simulator
These programs compute the total Bitcoin reward sizes, and the actual total supply of bitcoins.



<b>Introduction</b>: These programs will show the two different ways to calculate the total supply of Bitcoin. There is the standard way which most people understand as the total supply of BTC, which is 21,000,000 BTC. I then present the actual way BTC is calculated, which is not exactly 21,000,000 BTC.




The purpose of this project is to calculate the actual total supply of Bitcoin, which many assume is 21 million bitcoins.
That is actually not the exact number, and that requires some explanation.

<b>1. Bitcoin does not use decimals in division, it uses integer math.</b>

Integer Division in the Protocol

The Bitcoin protocol specifies that the block reward starts at 50 BTC and is halved after every 210,000 blocks. This halving is implemented as an integer division within the core logic of Bitcoin.   
When a halving occurs, the new reward is essentially the previous reward divided by 2. If the previous reward was an odd number of Satoshis (the smallest unit), this division would result in a fraction.
However, the protocol dictates that the block reward must be a whole number of Satoshis. Therefore, any fractional part resulting from the division is truncated (discarded).

<b>2. Bitcoin software protocol uses bit-shift operators.</b>

Bit-shift (Bitwise Shift) operators (<< for left shift and >> for right shift) are highly efficient ways to perform multiplication and division by powers of 2 at the binary level. They are crucial for 
optimizing various low-level operations within the Bitcoin software, such as integer arithmetic. Since satoshi (the smallest unit of Bitcoin) cannot have decimal values, these units must always be
expressed as whole integer values based on the Bitcoin protocol. Satoshis are used in the calculations and converted to Bitcoin. For example you can have a Satoshi value of 1375000, but not 1375000.3289 
(for example). Satoshis can only be whole numbers, so the decimal portion of any calculation result will be truncated.

******************************************************

Bitcoin's actual total supply is 20,999,999.9769 BTC, or 2,310,000 satoshis short of 21 million. 
This can be an interesting topic to discuss in Bitcoin and crypto circles.

Bitcoin truncates decimals when halving block rewards due to the way the reward schedule is defined within its protocol. That 
is why in explanation #1 decimals in division are discarded or truncated. The protocol will round the number to the nearest
whole integer value.

I present three programs in this project that are written in Python (version 3.6.5 and higher).

<b>TotalRewardSize.py :</b> This is the program that sums up all the Bitcoin reward sizes, not the total rewards given. It is a simple way to take each reward size value and
add it up. For example cycle 1 or the first block reward size was 50 BTC. When the halving came it was then 25 BTC, then 12.5 BTC ... until we reach 0 BTC. Add them all up and we get 100 BTC/block halvings.

<b>TotalBTCStandard.py:</b> This computes the total reward sizes only, not the total rewards issued (BTC created). This is taken from
each of the halving events, of which there are 33 significant halvings. Beyond that the protocol will continue the halving
process, but rewards will be insignificant to miners because they are at 0. 

The sum of all reward sizes from each halving totals to 
approximately 100 BTC/total blocks. When multiplied with the 210,000 halving blocks in each halving process we get the popular or more well known value of Bitcoin's approximate total supply of 21,000,000 BTC (i.e. all the BTC mined).

<b>TotalBitcoinSupply.py:</b> This presents the calculation of all the rewards of BTC issued, from the first block until the last significant 
block that issues BTC. This is how we arrive at the value 20,999,999.9769 BTC. This program correctly calculates the total amount of Bitcoin that will be mined by summing the rewards distributed in each halving era until the reward becomes zero. The result is very close to the theoretical limit of 21 million BTC.

The final amount of BTC that will be in circulation is 20,996,802.3669 BTC after removing 3,197.61 BTC from "burn addresses". These are permanently lost BTC that will never be put back into circulation. There are other reports that there can be as many as 3.7 million lost BTC (from a Chainalysis report), so that would make the supply in circulation even smaller.

******************************************************

The Bitcoin protocol defined using standard integer arithmetic to ensure clarity, reproducibility, and independence from specific hardware or low-level implementation details. This keeps the
protocol implementation simple, and removes the complexity of having to make changes with regards to precision.

******************************************************


