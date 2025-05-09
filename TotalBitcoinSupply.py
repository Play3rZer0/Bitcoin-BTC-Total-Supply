def calculate_total_satoshi_reward_detailed():
    """
    Calculates the total satoshi reward that will be mined throughout Bitcoin's history,
    and prints detailed information for each halving cycle.

    This function simulates the Bitcoin halving process, taking into account the integer
    division that occurs during each halving, which leads to a final total satoshi amount
    slightly less than the theoretical 21 million BTC.

    Returns:
        int: The total number of satoshis that will be mined.
    """

    # Initial block reward in satoshis (50 BTC * 100,000,000 satoshis/BTC)
    initial_reward_satoshi = 5_000_000_000

    # Current block reward in satoshis, which will be halved repeatedly
    block_reward_satoshi = initial_reward_satoshi

    # Number of blocks between each halving event
    halving_interval = 210_000

    # Running total of satoshis mined
    total_satoshi_reward = 0

    # Total number of blocks processed. This is used to limit the total ammount of blocks created
    block_count = 0

    # Halving cycle counter
    halving_count = 0

    # Loop until the block reward reaches 0 (no more blocks mined)
    while block_reward_satoshi > 0:
        # Calculate the number of blocks to process in this halving interval.
        # This is either the full halving interval, or the remaining amount of blocks left to mine.
        blocks_in_halving = min(halving_interval, (21_000_000 * 100_000_000 - block_count))

        # Calculate the total satoshis mined in this halving interval.
        rewards_for_interval = blocks_in_halving * block_reward_satoshi

        # Add the satoshis mined in this interval to the running total.
        total_satoshi_reward += rewards_for_interval

        # Increase the total block count by the blocks processed in this interval.
        block_count += blocks_in_halving

        # Print detailed information about this halving cycle.
        print(f"Halving {halving_count}:")
        print(f"  Block reward: {block_reward_satoshi} satoshis ({block_reward_satoshi / 100_000_000} BTC)")
        print(f"  Blocks in this halving: {blocks_in_halving}")
        print(f"  Total satoshis so far: {total_satoshi_reward} satoshis")
        print("-" * 20)

        # Halve the block reward for the next halving cycle using integer division.
        block_reward_satoshi //= 2

        # Increment the halving counter.
        halving_count += 1

    # Return the total number of satoshis mined.
    return total_satoshi_reward

def satoshi_to_btc(satoshi_amount):
    """
    Converts a satoshi amount to BTC.

    Args:
        satoshi_amount (int): The amount of satoshis to convert.

    Returns:
        float: The equivalent amount in BTC.
    """
    return satoshi_amount / 100_000_000

# Calculate the total satoshi reward.
total_satoshi = calculate_total_satoshi_reward_detailed()

# Convert the total satoshi reward to BTC.
total_btc = satoshi_to_btc(total_satoshi)

# Print the final results.
print(f"\nTotal satoshi reward: {total_satoshi} satoshis")
print(f"Total BTC reward: {total_btc} BTC")
