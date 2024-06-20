# 0x08. Making Change

## Project Overview
The "Making Change" project involves solving the classic coin change problem using algorithms. The goal is to determine the minimum number of coins needed to make up a given total amount, given a list of coin denominations. This project is a practical application of dynamic programming and greedy algorithms.

## Key Concepts

### Greedy Algorithms
- **Definition**: Algorithms that make the locally optimal choice at each stage with the hope of finding a global optimum.
- **Usage**: Suitable for certain cases of the coin change problem where the coin denominations allow for a straightforward solution.
- **Limitations**: May not always provide the optimal solution, especially with certain sets of coin denominations.

### Dynamic Programming
- **Definition**: A method for solving complex problems by breaking them down into simpler subproblems.
- **Principles**: Utilizes overlapping subproblems and optimal substructure.
- **Usage**: Often necessary for ensuring correctness and efficiency in solving the coin change problem.

### Algorithmic Complexity
- **Time Complexity**: Analyzing how the runtime of an algorithm scales with input size.
- **Space Complexity**: Analyzing the memory usage of an algorithm.
- **Optimization**: Striving for solutions with lower complexity to meet runtime constraints.

### Problem-Solving Strategies
- **Decomposition**: Breaking down the problem into smaller, manageable sub-problems.
- **Approaches**: Evaluating iterative vs recursive approaches in dynamic programming.

### Python Programming
- **Control Flow**: Using loops and conditional statements effectively.
- **Lists**: Manipulating lists and using list comprehensions.
- **Functions**: Implementing functions with efficient looping and conditional logic.

## Resources
- **Python Official Documentation**: For understanding control flow tools like loops and if statements.
- **GeeksforGeeks Articles**:
  - [Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)
  - [Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)
- **YouTube Tutorials**:
  - [Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=1R0_7HqNaW0)

## Requirements
- **Editors**: vi, vim, emacs
- **Environment**: Ubuntu 20.04 LTS using python3 (version 3.4.3)
- **File Conventions**: 
  - Files should end with a new line.
  - The first line should be `#!/usr/bin/python3`.
- **Style**: Code should follow PEP 8 style (version 1.7.x).
- **Executability**: All files must be executable.

## Task

### 0. Change Comes From Within
- **Objective**: Determine the fewest number of coins needed to meet a given amount total.
- **Prototype**: `def makeChange(coins, total)`
- **Return**: 
  - Fewest number of coins needed to meet `total`.
  - `0` if `total` is `0` or less.
  - `-1` if `total` cannot be met by any number of coins.
- **Constraints**:
  - `coins` is a list of the values of the coins in your possession.
  - The value of a coin is always an integer greater than `0`.
  - Assume an infinite number of each denomination of coin in the list.

### Example
```python
makeChange([1, 2, 25], 37)
# Output: 7

makeChange([1256, 54, 48, 16, 102], 1453)
# Output: -1
```

## Repository
- **GitHub Repository**: alx-interview
- **Directory**: 0x08-making_change
- **File**: 0-making_change.py
