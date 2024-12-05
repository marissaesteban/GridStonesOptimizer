# Grid Stones Optimizer

This project implements a computational geometry algorithm to solve grid-based queries. It centralizes coordinates, preprocesses spatial data with prefix sums, and calculates the maximum number of "stones" within a specified distance for each query. The code is structured to handle multiple test cases efficiently and output results for each case.

## Features

- **Coordinate Transformation**: Converts grid coordinates to a centralized system for easier computation.
- **Prefix Sum Preprocessing**: Creates a cumulative count matrix to optimize range queries.
- **Query Solver**: Computes the maximum number of stones within a given distance from any grid cell.
- **Dynamic Input Handling**: Processes input files with multiple test cases and outputs results in a standardized format.

## How It Works

1. **Input**: The algorithm reads from a file containing:
   - Grid dimensions (columns and rows).
   - Locations of stones in the grid.
   - Queries specifying a distance.
   
2. **Transformation**: Converts the input coordinates to a centralized system for simplified calculations.

3. **Prefix Sum Matrix**: Precomputes cumulative counts of stones across the grid to allow efficient sub-grid calculations.

4. **Query Evaluation**: Iterates over all possible grid cells to determine the maximum number of stones within the query distance.

5. **Output**: Prints the maximum stone count and corresponding coordinates for each query in each test case.
