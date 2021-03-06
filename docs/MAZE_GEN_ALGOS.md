# Maze-Generating Algorithms

#####Go back to the main [README](../README.md)


## Aldous-Broder

###### The Algorithm

1. Choose a random cell.
2. Choose a random neighbor of the current cell and visit it. If the neighbor has not yet been visited, add the traveled edge to the spanning tree.
3. Repeat step 2 until all cells have been visited.

###### Results

perfect, unbiased

###### Notes

This algorithm treats the cells of a maze as a graph, and solves to find a Uniform Spanning Tree that covers that graph. Like most tree-based maze algorithms, this one is a little slow.

## Backtracking Generator

###### The Algorithm

1. Randomly choose a starting cell.
2. Randomly choose a wall at the current cell and open a passage through it to any random, unvisited, adjacent cell. This is now the current cell.
3. If all adjacent cells have been visited, back up to the previous and repeat step 2.
4. Stop when the algorithm has backed all the way up to the starting cell.

###### Results

perfect, unbiased

###### Notes

This is perhaps the most common maze-generation algorithm because it is easy to understand and implement. And it produces high-quality mazes.

## Binary Tree

###### The Algorithm

1. For every cell in the grid, knock down a wall either North or West.

###### Optional Parameters

* *bias*: String {'NW', 'NE', 'SE', 'SW'}
 * Determines which corner of the maze to start looping from. Thus, it also determines the direction of the bias inherant in this algorithm. (default 'NW')

###### Results

perfect, biased, flawed

###### Notes

This algorithm produces mazes with a serious flaw: the North and West borders of the maze are completely open. Generally, this makes solving the maze too easy to be fun. However, if the person solving the maze can't see the entire thing at one time, this algorithm is still useful.

On the positive side, this algorithm is extremely fast and very easy to implement.

## Cellular Automaton

###### The Algorithm

Cells survive if they have one to four neighbours. If a cell has exactly three neighbours, it is born. It is similar to Conway's Game of Life in that patterns that do not have a living cell adjacent to 1, 4, or 5 other living cells in any generation will behave identically to it.

###### Optional Parameters

* *comlpexity*: Float [0.0, 1.0]
 * Determines the number of times to seed from a given cell. (default 1.0)
* *density*: Float [0.0, 1.0]
 * Determines how many cells to seed from. (default 1.0)

###### Results

perfect, unbiased

###### Notes

Using Cellular Automation to generate a maze is a really fun idea, but it is definitely the slowest maze-generating algorithm. And even though the result is a "perfect" maze, it is frequently very easy to solve.

More research is needed to create a post-processing step to remove the typical Cellular Automaton defects.

## Dungeon Rooms

###### The Algorithm

This is a variation on Hunt-and-Kill where the initial maze has rooms carved out of it, instead of being completely filled.

###### Optional Parameters

* *rooms*: List(List(tuple, tuple))
 * A list of lists, containing the top-left and bottom-right grid coords of where you want rooms to be created. For best results, the corners of each room should have odd-numbered coordinates.
* *grid*: MazeArray
 * A pre-built maze array filled with one, or many, rooms.
* *hunt_order*: String ['random', 'serpentine']
 * Determines how the next cell to hunt from will be chosen. (default 'random')

###### Results

imperfect. unbiased.

###### Notes

Theseus traversed a maze to find a minotaur in the center. Similar things happen in a lot of games; players will traverse a maze to find a room filled with enemies or treasure. I developed this algorithm to aid this use-case.

## Eller's

###### The Algorithm

1. Put the each cell of the first row in its own set.
2. Join adjacent cells. But not if they are already in the same set. Merge the sets of these cells.
3. For each set in the row, create at least one vertical connection down to the next row.
4. Put any unconnected cells in the next row into their own set.
5. Repeat steps 2 through 4 until the last row.
6. In the last row, join all adjacent cells that do not share a set.

###### Optional Parameters

* *xbias*: Float [0.0, 1.0]
 * Probability of joining cells in the same row. (default 0.5)
* *ybias*: Float [0.0, 1.0]
 * Probability of joining cells in the same column. (default 0.5)

###### Results

perfect. unbiased.

###### Notes

This is a classic set-theory algorithm. It is not the fastest algorithm, as it requires relabeling whole sets of cells at every step.

## Growing Tree

###### The Algorithm

1. Let C be a list of cells, initially empty. Add one a random cell from the maze to C.
2. Choose a cell from C, and carve a passage to any unvisited neighbor of that cell, adding that neighbor to C as well. If there are no unvisited neighbors, remove the cell from C.
3. Repeat step 2 until C is empty.

###### Optional Parameters

* *backtrack_chance*: Float [0.0, 1.0]
 *  Splits the logic to either use Recursive Backtracking (RB) or Prim's (random) to select the next cell to visit. (default 1.0)

###### Results

perfect. unbiased.

###### Notes

This algorithm is very flexible. Instead of defining exactly what must be done, it lays out a general construct. The exact order in which we choose a new cell from set C in step 2 is left undefined. That means we can pick one at random (and mimick the Prim's algorithm), or always pick the most recent one (and mimick the Backtracking algorithm). This implementation allows the developer to set the percentage of time Backtracking is chosen versus Prim's. This gives a lot of variety to the final complexity and look of the final maze.

## Hunt-and-Kill

###### The Algorithm

1. Randomly choose a starting cell.
2. Perform a random walk from the current cell, carving passages to unvisited neighbors, until the current cell has no unvisited neighbors.
3. Select a new grid cell; if it has been visited, walk from it.
4. Repeat steps 2 and 3 a sufficient number of times that there the probability of a cell not being visited is extremely small.

###### Optional Parameters

* *hunt_order*: String ['random', 'serpentine']
 * Determines how the next cell to hunt from will be chosen. (default 'random')

###### Results

perfect. unbiased.

###### Notes

Generally, you might think random-walk algorithms are very slow. But Hunt-and-Kill is quite efficient. And I really like the end results of this algorithm: the mazes are not easy to solve.

In this implementation of Hunt-and-kill there are two different ways to select a new grid cell in step 2. The first is serpentine through the grid (the classic solution), the second is to randomly select a new cell enough times that the probability of an unexplored cell is very, very low. The second option includes a small amount of risk, but it creates a more interesting, harder maze. Thus, the second option is default in this implementation.

## Kruskal's

###### The Algorithm

1. Create a set of all walls in the grid.
2. Randomly select a wall from the grid. If that wall connects two disjoint trees, join the trees. Otherwise, remove that wall from the set.
3. Repeat step 2 until there are no more walls left in the set.

###### Results

perfect. unbiased.

###### Notes

Like Prim's, it is based on a namesake algorithm for finding a Minimal Spanning Tree (MST) over a graph.

## Perturbation

###### The Algorithm

1. Start with a complete, valid maze.
2. Add a small number of random walls, blocking current passages.
3. Go through the maze and reconnect all passages that are not currently open, by randomly opening walls.
4. Repeat steps 3 and 4 a prescribed number of times.

###### Optional Parameters

* *new_walls*: Integer [1, ...)
 * The number of randomly positioned new walls you create throughout the maze. (default 1)
* *repeat*: Integer [1, ...)
 * The number of times sets of new walls will be added to the maze; the maze being fixed after each set. (default 1)

###### Results

unbiased.
perfect if-and-only-if the input maze was perfect.

###### Notes

In math and physics, perturbation theory is idea that you can solve a new problem by starting with the known solution to an old problem and making a small change. Here, we take a solved maze and perturb it slightly by adding a couple walls, then re-solve the maze. This is an amazingly powerful tool. It can fix nearly any flaw in a maze. Or you can start with a non-maze, say a nice spiral or a cute drawing, and turn it into a maze using first-order perturbations.

With great power comes great responsibility. If you use this method on a grid that does not contain a maze, it will fail. If you run too many iterations of this algorithm, your end maze will look nothing like the original. But if used wisely, this is an extremely powerful tool.

## Prim's

###### The Algorithm

1. Choose an arbitrary cell from the grid, and add it to some (initially empty) set visited nodes (V).
2. Randomly select a wall from the grid that connects a cell in V with another cell not in V.
3. Add that wall to the Minimal Spanning Tree (MST), and the edge’s other cell to V.
4. Repeat steps 2 and 3 until V includes every cell in G.

###### Results

perfect. unbiased.

###### Notes

This is a classic. Like Kruskal's, it is based on the idea of finding a MST in a graph. But Prim's is purely random. In fact, randomized variations on other maze-generating algorithms are frequently called "Prim's variations".

## Recursive Division

###### The Algorithm

1. Start with an empty grid.
2. Build a wall that bisects the grid (horizontal or vertical). Add a single passage through the wall.
3. Repeat step 2 with the areas on either side of the wall.
4. Continue, recursively, until the maze passages are the desired resolution.

###### Results

perfect. biased.

###### Notes

The algorithm is very simple to understand, and reasonably simple to implement. But the results will always look skewed. A big line that perfect divides a maze makes it easier for the human eye to solve: it reduces your visual search space. This is doubly true for humans that happen to know the maze was created by division.

This implementation tries, as far as is possible, to reduce these biases by alternating the cuts between horizontal and vertical. (Obviously, if you made 7 vertical cuts in a row the maze would be very easy to solve.)

## Sidewinder

###### The Algorithm

1. Select cells in the maze, row-by-row.
2. Add the current cell to a “run” set.
3. For the current cell, randomly decide whether to carve East.
4. If a passage East was carved, make the new cell the current cell and repeat steps 2-4.
5. If a passage East was not carved, choose any one of the cells in the run set and carve a passage North. Then empty the run set. Repeat steps 2-5.
6. Continue until all rows have been processed.

###### Optional Parameters

* *bias*: Float [0.0, 1.0]
 * If the bias is set less than 0.5 the maze will be biased East-West, if it set greater than 0.5 it will be biased North-South. (default 0.5)

###### Results

perfect. unbiased. flawed.

###### Notes

The algorithm is simple and optimally fast. However, the North side of the maze will always be one, long, open corridor. For my tastes, this makes the maze too easy to solve. There are use-cases where that will not matter though; if the person solving the maze cannot see the whole thing at one time.

Research is needed to create a post-processing step to fix this flaw.


## Wilson's

###### The Algorithm

1. Choose a random cell and add it to the Uniform Spanning Tree (UST).
2. Select any cell that is not in the UST and perform a random walk until you find a cell that is.
3. Add the cells and walls visited in the random walk to the UST.
4. Repeat steps 2 and 3 until all cells have been added to the UST.

###### Optional Parameters

* *hunt_order*: String ['random', 'serpentine']
 * Determines how the next cell to hunt from will be chosen. (default 'random')

###### Results

perfect. unbiased.

###### Notes

Like all random-walk algorithms, Wilson's isn't terribly fast. However, this still converges faster than Aldous-Broder. And it produces similarly nice results.


#####Go back to the main [README](../README.md)

