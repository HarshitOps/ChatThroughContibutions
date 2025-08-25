def left_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

def right_triangle(n):
    for i in range(1, n + 1):
        print("  " * (n - i) + "* " * i)

def pyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))