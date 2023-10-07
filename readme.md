## Knapsack Problem Solver

This project provides a Python implementation of two algorithms to solve the 0-1 Knapsack Problem - Dynamic Programming and Greedy Algorithm. It also includes utilities to read test cases from data files, perform the algorithmic computations, and generate CSV reports and bar chart visualizations to compare the results.

### Table of Contents

1. [Introduction](#introduction)
2. [Usage](#usage)
   - [Running the Algorithms](#running-the-algorithms)
   - [Generating CSV Reports](#generating-csv-reports)
   - [Creating Bar Chart Visualizations](#creating-bar-chart-visualizations)
3. [Algorithm Details](#algorithm-details)
   - [Dynamic Programming](#dynamic-programming)
   - [Greedy Algorithm](#greedy-algorithm)
4. [Sample Data](#sample-data)
5. [Requirements](#requirements)
6. [Example Usage](#example-usage)
7. [Contributing](#contributing)
8. [License](#license)

### Introduction

The 0-1 Knapsack Problem involves finding the maximum value that can be obtained by selecting a subset of items, each with its own weight and value, to fit into a knapsack with a limited weight capacity. The two algorithms provided here aim to solve this problem:

- **Dynamic Programming:** This algorithm uses dynamic programming techniques to compute the maximum value that can be obtained while respecting the weight capacity of the knapsack. It also returns the indices of the selected items.

- **Greedy Algorithm:** The greedy algorithm solves the problem by selecting items based on their value-to-weight ratio in a descending order. It keeps adding items to the knapsack until it reaches the weight capacity. This algorithm also returns the maximum value and the indices of selected items.

### Usage

#### Running the Algorithms

To run the algorithms on test cases, follow these steps:

1. Place your test case data files in the `data/instances` directory.

2. Open the Python script you want to use (e.g., `knapsack_dynamic_programming.py` or `knapsack_greedy.py`).

3. Modify the `data_directory` variable to specify the directory where your test cases are stored.

4. If you want to limit the number of test cases to run, set the `tested` variable to the desired number. For example, `tested = 10` will run the first 10 test cases.

5. Execute the script to run the selected algorithm on the test cases and view the results.

#### Generating CSV Reports

The scripts automatically generate CSV reports for the algorithm results. The reports include details such as the test case number, knapsack capacity, maximum values, execution times, and whether the dynamic programming or greedy algorithm performed better. The CSV files are saved in the `data/results` directory.

#### Creating Bar Chart Visualizations

The provided script `bar_chart_visualization.py` generates a bar chart visualization to compare the results of the dynamic programming and greedy algorithms for the test cases. The bar chart displays the maximum values achieved by each algorithm for each test case.

### Algorithm Details

#### Dynamic Programming

The Dynamic Programming algorithm uses a bottom-up approach to compute the maximum value that can be obtained within the weight capacity of the knapsack. It creates a dynamic programming table to store intermediate results. The algorithm also returns the indices of the selected items that contribute to the maximum value.

#### Greedy Algorithm

The Greedy Algorithm solves the problem by selecting items based on their value-to-weight ratio in descending order. It adds items to the knapsack until it reaches the weight capacity limit. The algorithm returns the maximum value achieved and the indices of the selected items.

### Sample Data

Sample test case data is provided in the `data/instances` directory. You can use these data files to test the algorithms.

### Requirements

To run this project, you need to have the following Python packages installed:

- `matplotlib` (Version 3.4.3)
- `numpy` (Version 1.21.2)

You can install these packages using `pip` with the command:

```bash
pip install -r requirements.txt
```

### Example Usage

Here's an example of how to use this project to solve 20 instances of the Knapsack Problem and visualize the results:

1. Place your test case data files (e.g., `instance1.txt`, `instance2.txt`, ...) in the `data/instances` directory.

2. Open the Python script you want to use (e.g., `knapsack_dynamic_programming.py` or `knapsack_greedy.py`).

3. Modify the `data_directory` variable to specify the directory where your test cases are stored.

4. Set `tested` to `20` to run 20 test cases.

5. Execute the script.

6. Run the `bar_chart_visualization.py` script to generate a bar chart visualization of the results:

```bash
python bar_chart_visualization.py
```

You will see a bar chart similar to the example image below, comparing the results of the Dynamic Programming and Greedy Algorithm for each test case:

![Knapsack Algorithm Comparison](example-output.png)

### Contributing

Contributions to this project are welcome. If you have suggestions, improvements, or additional features to add, please feel free to submit a pull request.

### License

This project is licensed under the MIT License. You can find the full license in the `LICENSE` file.
