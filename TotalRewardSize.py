# Program to calculate the total supply of Bitcoin based on halving cycle and reward sizes
# This is the simple way to calculate the total Bitcoin supply, but is not exact

def calculate_total_bitcoin_supply():
    
    # Calculates the total Bitcoin that will ever be mined based on the halving cycle and total reward sizes.

    initial_reward = 50.0
    halving_interval = 210000
    reward = initial_reward
    total_bitcoin = 0.0

    # This loop will continue as long as the reward size is greater than 0.

    while reward > 0:
        rewards_in_cycle = halving_interval * reward
        total_bitcoin += rewards_in_cycle
        reward /= 2

    return total_bitcoin

# The total BTC supply using this program will return 21,000,000 BTC.
# This is based on the total of all reward sizes multiplied with the 210,000 halving interval

if __name__ == "__main__":
    total_btc = calculate_total_bitcoin_supply()
    print(f"\nResult: The total Bitcoin supply will be approximately {total_btc} BTC.")
