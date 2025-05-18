def calculate_sum_of_rewards():
    #Calculates the sum of all future Bitcoin block reward sizes.
    initial_reward = 50.0
    reward = initial_reward
    sum_of_rewards = 0.0

    while reward > 0:
        sum_of_rewards += reward
        reward /= 2

    return sum_of_rewards

if __name__ == "__main__":
    total_reward_sizes = calculate_sum_of_rewards()
    print(f"\nResult: The sum of the Bitcoin block reward sizes will be approximately {total_reward_sizes} BTC.")
