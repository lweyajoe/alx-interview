#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []

    pascal = []

    for i in range(n):
        row = [1]  # The first element in each row is always 1

        # Calculate the elements in the current row
        if i > 0:
            for j in range(1, i):
                # Calculate each element by summing the two elements above it
                element = pascal[i - 1][j - 1] + pascal[i - 1][j]
                row.append(element)

            row.append(1)  # The last element in each row is always 1

        pascal.append(row)

    return pascal

# Example usage:
# n = 5
#  result = pascal_triangle(n)
#  for row in result:
#    print(row)
