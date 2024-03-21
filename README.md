Certainly! Below is a structured README file tailored for your project, which involves implementing a search engine for solving the "X puzzle" using various search algorithms.

---

# X Puzzle Solver

## Overview

This project is an implementation of a search engine designed to solve the "X puzzle". The puzzle consists of a game board of size NxN, where one slot is empty, and the others contain numbers from 1 to (N*N - 1) arranged in any order. The objective is to move the squares strategically so that they align in ascending order with the empty slot at the end. This README outlines the problem, our approach, and how to run the program.

## Problem Description

- **Board Setup:** An NxN grid with one empty slot and the remaining slots filled with numbers from 1 to N*N - 1.
- **Goal:** Arrange the squares in ascending order with the empty slot at the end.
- **Movements:** You can move a square up, down, left, or right into the empty slot, provided the move is valid.
- **Move Cost:** Each move costs 1.
- **Algorithms:** The program supports various search algorithms, including IDS (1), BFS (2), A* (3), and IDA* (4).

## Input/Output Format

- **Input:** The program reads from `input.txt`, which includes:
  - The algorithm code (1-4) on the first line.
  - The board size (N) on the second line.
  - The initial board state on the third line, represented as numbers separated by dashes (`-`).

- **Output:** The program writes to `output.txt`, describing the solution as a series of moves: R (right), L (left), D (down), and U (up).

## Implementation Details

- **Close List:** An additional CLOSE LIST is used to track visited states.
- **Vertex Management:** Vertices are ordered by their creation time and, if equal, by the move that generated them in the order: up, down, left, right.
- **Manhattan Distance:** Informed algorithms use the Manhattan distance heuristic to estimate the cost to reach the goal.

## Running the Program

1. Prepare the `input.txt` file in the project's root directory with the algorithm code, board size, and initial board state.

2. Run the program (assuming it's a Python script):

   ```bash
   python puzzle_solver.py
   ```

3. Check the `output.txt` file for the solution path.

## Example

### input.txt

```
2
4
1-2-3-4-5-6-7-8-9-10-11-12-13-0-14-15
```

### output.txt

```
LL
```

## Contributing

Feel free to fork the repository, make improvements, and submit pull requests. We appreciate your contributions to enhancing this puzzle solver!

## License

This project is open-source and available under the MIT License.

---

Adjust this template as necessary to fit the specifics of your project, and ensure that any placeholder text is replaced with the actual details of your project. This README is designed to give a clear, concise overview of your project and how it can be used.
