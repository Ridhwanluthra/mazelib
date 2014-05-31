
from random import choice,shuffle
from MazeSolveAlgo import MazeSolveAlgo
from ShortestPaths import ShortestPaths


class DeadEndFiller(MazeSolveAlgo):
    """
    This is a simple Maze solving algorithm.
    It focuses on the Maze, is always very fast, and uses no extra
    memory.

    Just scan the Maze, and fill in each dead end, filling in the
    passage backwards from the block until you reach a junction. This
    includes filling in passages that become parts of dead ends once
    other dead ends are removed. At the end only the solution will
    remain, or solutions if there are more than one.
    
    What is left is a maze with only solution tiles. Loop through
    these cells and build the solution(s).

    This will always find the one unique solution for perfect Mazes,
    but won't do much in heavily braid Mazes, and in fact won't do
    anything useful at all for those Mazes without dead ends.
    """
    def _solve(self):
        self.grid[self.start] = self.grid[self.end] = 0
        current = self.start

        # loop through the maze serpentine, and find dead ends
        dead_end = self._find_dead_end()
        while dead_end != (-1, -1):
            # fill-in and wall-off the dead end
            self._fill_dead_end(dead_end)
            
            # from the dead end, travel one cell.
            ns = self._find_unblocked_neighbors(dead_end)
            
            if len(ns) == 0: break

            # look at the next cell, if it is a dead end, restart the loop
            if len(ns) == 1:
                # continue until you are in a junction cell.
                if self._is_dead_end(ns[0]):
                    dead_end = ns[0]
                    continue

            # otherwise, find another dead end in the maze
            dead_end = self._find_dead_end()

        solutions = self._build_solutions()
       
        return solutions
    
    def _build_solutions(self):
        """Now that all of the dead ends have been cut out, the maze still needs to be solved."""
        s = ShortestPaths()

        return s.solve(self.grid, self.start, self.end)

    def _fill_dead_end(self, dead_end):
        """After moving from a dead end, we want to fill in it and all
        the walls around it.
        """
        r,c = dead_end
        self.grid[r, c] = 1
        self.grid[r - 1, c] = 1
        self.grid[r + 1, c] = 1
        self.grid[r, c - 1] = 1
        self.grid[r, c + 1] = 1

    def _find_dead_end(self):
        """A "dead end" is a cell with only zero or one open neighbors.
        The start end end count as open.
        """
        for r in xrange(1, self.grid.height, 2):
            for c in xrange(1, self.grid.width, 2):
                if (r, c) in [self.start, self.end]:
                    continue
                if self._is_dead_end((r, c)):
                    return (r, c)

        return (-1, -1)

    def _is_dead_end(self, cell):
        """A dead end has zero or one open neighbors."""
        ns = self._find_neighbors(cell)
        #ns = self._find_unblocked_neighbors(cell)
        if self.grid[cell] == 1:
            return False
        elif len(ns) in [0, 1]:
            return True
        else:
            return False

    def _find_unblocked_neighbors(self, posi, visited=True):
        """Find all the grid neighbors of the current position;
        visited, or not.
        """
        (row, col) = posi
        ns = []

        if row > 1 and self.grid[row-1, col] != visited and self.grid[row-2, col] != visited:
            ns.append((row-2, col))
        if row < self.grid.height-2 and self.grid[row+1, col] and self.grid[row+2, col] != visited:
            ns.append((row+2, col))
        if col > 1 and self.grid[row, col-1] and self.grid[row, col-2] != visited:
            ns.append((row, col-2))
        if col < self.grid.width-2 and self.grid[row, col+1] and self.grid[row, col+2] != visited:

            ns.append((row, col+2))

        shuffle(ns)

        return ns

    def _find_neighbors(self, posi, visited=True):
        """Find all the grid neighbors of the current position;
        visited, or not.
        """
        (row, col) = posi
        ns = []

        if row > 1 and self.grid[row-2, col] != visited:
            ns.append((row-2, col))
        if row < self.grid.height-2 and self.grid[row+2, col] != visited:
            ns.append((row+2, col))
        if col > 1 and self.grid[row, col-2] != visited:
            ns.append((row, col-2))
        if col < self.grid.width-2 and self.grid[row, col+2] != visited:

            ns.append((row, col+2))

        shuffle(ns)

        return ns
