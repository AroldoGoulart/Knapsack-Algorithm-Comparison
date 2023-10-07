def knapsack_greedy(values, weights, capacity):
    n = len(values)
    value_per_weight = [(values[i] / weights[i], values[i], weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)

    max_value = 0
    selected_items = [0] * n  # Inicialmente, nenhum item é selecionado

    for _, v, w, i in value_per_weight:
        if capacity >= w:
            max_value += v
            capacity -= w
            selected_items[i] = 1  # Marca como selecionado (binário)

    return max_value, selected_items
