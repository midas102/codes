def knapSack_DP(capacity, item_weights, item_values, num_items):
    # Create a 2D array dp to store the maximum value for each subproblem
    dp = [[0 for weight in range(capacity + 1)] for item in range(num_items + 1)]
    
    # Build the DP table dp[][] in a bottom-up manner
    for item in range(num_items + 1):
        for weight in range(capacity + 1):
            if item == 0 or weight == 0:
                dp[item][weight] = 0  # Initialize the first row and first column with 0
            elif item_weights[item - 1] <= weight:
                # Include the item and exclude the item, take max of both
                dp[item][weight] = max(
                    item_values[item - 1] + dp[item - 1][weight - item_weights[item - 1]], 
                    dp[item - 1][weight]
                )
            else:
                # If item cannot be included, inherit value from the cell above
                dp[item][weight] = dp[item - 1][weight]
    
    return dp[num_items][capacity]  # Return the maximum value for the full capacity and all items

# Example usage
item_values = [60, 100, 120]  # Values of items
item_weights = [10, 20, 30]   # Weights of items
capacity = 50                 # Knapsack capacity
num_items = len(item_values)  # Number of items

print("Maximum value in the knapsack:", knapSack_DP(capacity, item_weights, item_values, num_items))
