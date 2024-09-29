#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []

    for row in range(n):
        new_row = [None] * (row + 1)
        new_row[0] = 1
        new_row[-1] = 1

        for i in range(1, row):
            new_row[i] = triangle[row - 1][i - 1] + triangle[row - 1][i]

        triangle.append(new_row)
    return triangle
