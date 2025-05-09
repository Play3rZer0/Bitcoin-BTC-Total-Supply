# Bitcoin-BTC-Calculator
These programs compute the total Bitcoin reward sizes, and the actual total supply of bitcoins.

The purpose of this project is to calculate the actual total supply of Bitcoin, which many assume is 21 million bitcoins.
That is actually not the exact number, and that requires some explanation.

1. Bitcoin does not use decimals in division, it uses integer math.
2. Bitcoin software protocol uses bitshift-operators.

Bitcoin's actual total supply is 20,999,999.9769 BTC, or 2,310,000 satoshis short of 21 million. 
(If you want to be a lot of fun at parties, bring this up whenever someone says that the maximum number of Bitcoins is 21 million.)
