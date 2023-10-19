# Depth-First Search (DFS) and Breadth-First Search (BFS) Algorithms in Python
#### Video Demo: [...]

## Description:
The project is a Python program that demonstrates the Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms for graph traversal. These algorithms are fundamental in graph theory and can be used to explore or search through connected graph-like data structures.

## Overview

Graph traversal is a common problem in computer science and is used for a wide range of applications, including pathfinding, network analysis, and more. This Python program provides a practical example of how to implement DFS and BFS algorithms to navigate and search through a graph.

### Depth-First Search (DFS)

Depth-First Search is an algorithm used to traverse or search a graph or tree data structure. The DFS algorithm starts at the root node and explores as far as possible along each branch before backtracking. It is implemented using a stack data structure or recursion.

### Breadth-First Search (BFS)

Breadth-First Search is another algorithm for graph traversal that systematically explores all the vertices and edges at the current level before moving to the next level. It uses a queue data structure to keep track of the vertices to be visited.

## File Contents

- `pathalgo.py`: This Python file contains the main program that demonstrates the DFS and BFS algorithms on a sample graph.
- `node.py`: This file defines the `Node` class, which is used to creat different nodes and keep track of its parent
- `maze.txt`: This file contains the maze used to test the program. Different type of maze can be used as long as it follows the specified rule
- `test_pathalgo.py`: This file contains the program that is used to test different section of the main program using pytest module

## Usage

To use this Python program to demonstrate DFS and BFS algorithms, follow these steps:

1. Clone the repository to your local machine using Git:

   ```bash
   git clone [repository URL]
2. Change the working directory to the project folder:
    cd file-python

3. Run the python program:
    python pathalgo.py maze.txt (DFS or BFS)

## Design Choices
The project is designed to be a simple and illustrative demonstration of DFS and BFS algorithms. The graph is intentionally small to keep the code concise and focused on the algorithm's logic.

The program provides both DFS and BFS implementations to showcase the differences between these two traversal methods.
