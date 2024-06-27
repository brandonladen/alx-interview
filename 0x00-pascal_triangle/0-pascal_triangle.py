#!/usr/bin/python3
"""
pascal triangle
"""

def pascal_triangle(n):
    # Return an empty list if n is less than or equal to 0
    if type(n) is not int or n <= 0:
        return []
    
    # Initialize the triangle with the first row
    res = [[1]]

    # Build the Pascal's Triangle row by row
    for i in range(1, n):
        # Create the new row by adding 0 at both ends of the previous row
        temp = [0] + res[-1] + [0]
        row = []
        # Sum adjacent elements to create the new row
        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        res.append(row)
    
    return res
