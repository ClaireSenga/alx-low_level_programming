#!/usr/bin/python3

def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid
    
    Args:
    - grid (list of list of integers): Represents island where:
        - 0 represents a water zone.
        - 1 represents a land zone
    
    Returns:
    - perimeter (int): The perimeter of the island
    
    Constraints:
    - Grid is rectangular, width & height don’t exceed 100
    - Grid is completely surrounded by water, & there is one island (or none)
    - The island doesn’t have “lakes” (water inside that isn’t connected to the water around the island)
    """

    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1
    
    return perimeter
