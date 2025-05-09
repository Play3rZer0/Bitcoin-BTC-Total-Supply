# Program to calculate the total supply of Bitcoin based on halving cycle and reward sizes

def calculate_total_bitcoin_supply():
    #Calculates the total Bitcoin that will ever be mined.
    initial_reward = 50.0
    halving_interval = 210000
    reward = initial_reward
    total_bitcoin = 0.0

    while reward > 0:
        rewards_in_era = halving_interval * reward
        total_bitcoin += rewards_in_era
        reward /= 2

    print(f"The total amount of Bitcoin that will ever be mined is: {total_bitcoin} BTC")
    return total_bitcoin

if __name__ == "__main__":
    total_btc = calculate_total_bitcoin_supply()
    print(f"\nResult: The total Bitcoin supply will be approximately {total_btc} BTC.")
