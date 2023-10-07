from src.dynamic import dynamic_programming
from src.greedy import knapsack_greedy
from utils.reader import load_test_cases
import csv

data_directory = "data/instances"
csv_filename = "data/results/comparation.csv"

test_cases = load_test_cases(data_directory)

results = []

# ler apenas o primeiro arquivo
for i, test_case in enumerate(test_cases[:1]):
    values = test_case["values"]
    weights = test_case["weights"]
    capacity = test_case["capacity"]

    [max_value_dynamic, selected_items_dynamic] = dynamic_programming(values, weights, capacity)
    [max_value_greedy, selected_items_greedy] = knapsack_greedy(values, weights, capacity)

    print(f"Test Case {i + 1}:")
    print(f"Dynamic Programming: {max_value_dynamic}")
    print(f"Greedy: {max_value_greedy}")
    print()
    results.append({
        "Test-Case": i + 1,
        "Capacity": capacity,
        "Best": max_value_dynamic if max_value_dynamic > max_value_greedy else max_value_greedy,
        "Dynamic-Programming": max_value_dynamic,
        "Greedy": max_value_greedy,
    })

with open(csv_filename, mode='w', newline='') as csv_file:
    fieldnames = ["Test-Case", "Capacity", "Best", "Dynamic-Programming", "Greedy"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)