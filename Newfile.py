def left_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

def right_triangle(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))

def square(n):
    for i in range(n):
        print("* " * n)


# Driver code
rows = 5
print("Left Triangle:")
left_triangle(rows)


print("\nRight Triangle:")
right_triangle(rows)


print("\nPyramid:")
pyramid(rows)

print("\nSquare:")
square(rows)
