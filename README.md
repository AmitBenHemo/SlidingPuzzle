# AI-Algorithms
The problem:
You must implement a search engine that supports several search algorithms to solve the following problem: "the X puzzle".
Given a game board of size NxN, where one slot is empty and each of the other slots contains a number
from 1 to (n*n -1) in some order when the goal is to move the squares so that they are displayed in the goal position.
The goal state is defined to be an ascending order of the numbers with the empty slot at the end.

movement:
At each step you can move one of the numbered squares towards the empty square. when the options
The ones available to us are up, down, right, left - any of the options when possible.
For Dodge: In the picture above, the above option is not possible.
The cost of each move is fixed - a cost of 1.
realization:
Input - The program will read its input from a single input.txt file.
  The first line in the file will determine which algorithm to use: we will support several search algorithms according to the following coding:
1 for IDS,
2 for BFS,
3 for A*,
4 for *IDA.
The size of the board will be written in the second line.
In the third line will be written the initial state of the game board.
Output - the program will write into a file called output.txt and it will contain one line in the following format:
A route is described by the series of actions required to get from the starting state to the ending state. The actions are R
(right), L (left), D (down) and U (up). Capital letters must be used.
For Dodge: RDRU describes a course of right, down, right and up.

On vertices of the same importance, we will apply the following order relation:
First we will arrange according to the production time of the vertex. If several vertices were created at the same time (common ancestor)
The vertices will be arranged according to the following order: up, down, left, right.
In summary: the vertices will be arranged according to: the requirements of the algorithm and then according to the operator that created them according to the above order.

Note: in the implementation of all the above-mentioned algorithms, an additional CLOSE LIST must also be used.
Check: if a child vertex is already in one of the (OPEN \ (CLOSE) lists, there is no need to insert the vertex at all.
In known algorithms, if a child vertex is already in the CLOSE LIST, there is no need to insert the vertex at all. If we are in the OPEN LIST, and now we have received a new value lower than what the same vertex has in the OPEN LIST, the OPEN LIST must be updated with the new value.

In implementing the informed algorithms I used the Manhattan distance function.
Example for: input.txt:
2
4
1-2-3-4-5-6-7-8-9-10-11-12-13-0-14-15

Example for output.txt:
LL
