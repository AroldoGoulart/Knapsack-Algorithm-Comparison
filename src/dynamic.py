def dynamic_programming(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    selected_items = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                without_this_item = dp[i - 1][w]
                with_this_item = dp[i - 1][w - weights[i - 1]] + values[i - 1]

                if with_this_item >= without_this_item:
                    dp[i][w] = with_this_item
                    selected_items[i][w] = 1
                else:
                    dp[i][w] = without_this_item
            else:
                dp[i][w] = dp[i - 1][w]

    # Items selecionados
    selected = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if selected_items[i][w] == 1:
            selected.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected
