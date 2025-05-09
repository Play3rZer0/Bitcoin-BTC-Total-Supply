def calculate_all_btc_rewards():
    """
    Calculates and lists all Bitcoin block rewards in BTC for each halving era.

    Returns:
        tuple: A tuple containing:
            - list: A list of BTC rewards for each halving era.
            - float: The total BTC reward issued.
    """

    initial_reward_btc = 50.0
    block_reward_btc = initial_reward_btc
    halving_interval = 210_000
    all_rewards_btc = []
    total_btc_reward = 0.0
    block_count = 0
    halving_count = 0

    while block_reward_btc > 1e-9:  # Continue until reward is very small
        blocks_in_halving = min(halving_interval, (21_000_000 - (block_count / 100_000))) # Approximate blocks
        reward_for_era = blocks_in_halving * block_reward_btc
        all_rewards_btc.append(reward_for_era)
        total_btc_reward += reward_for_era
        block_count += blocks_in_halving
        block_reward_btc /= 2.0
        halving_count += 1

    return all_rewards_btc, total_btc_reward

all_rewards, total_btc = calculate_all_btc_rewards()

print("Bitcoin Rewards per Halving Era (BTC):")
for i, reward in enumerate(all_rewards):
    print(f"Halving {i}: {reward:.8f} BTC")

print(f"\nTotal Estimated BTC Reward: {total_btc:.8f} BTC")
