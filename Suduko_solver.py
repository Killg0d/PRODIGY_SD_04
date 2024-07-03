def get_user_input():
    print("Enter the Sudoku puzzle row by row, with 0s representing empty cells:")
    puzzle = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i + 1}: ").split()))
                if len(row) == 9 and all(0 <= num <= 9 for num in row):
                    puzzle.append(row)
                    break
                else:
                    print("Please enter exactly 9 numbers between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
    return puzzle

# Get Sudoku puzzle from user
arr = get_user_input()


# Utility functions to track the constraints
rows = [set() for _ in range(9)]
cols = [set() for _ in range(9)]
subgrids = [set() for _ in range(9)]

def get_subgrid_index(x, y):
    return (x // 3) * 3 + (y // 3)

# Initialize the sets with the initial numbers
for i in range(9):
    for j in range(9):
        if arr[i][j] != 0:
            rows[i].add(arr[i][j])
            cols[j].add(arr[i][j])
            subgrids[get_subgrid_index(i, j)].add(arr[i][j])

def printMatrix():
    for row in arr:
        print(" ".join(str(num) for num in row))

def is_safe(x, y, num):
    return (num not in rows[x] and 
            num not in cols[y] and 
            num not in subgrids[get_subgrid_index(x, y)])

def solve():
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for num in range(1, 10):
                    if is_safe(i, j, num):
                        arr[i][j] = num
                        rows[i].add(num)
                        cols[j].add(num)
                        subgrids[get_subgrid_index(i, j)].add(num)
                        
                        if solve():
                            return True
                        
                        arr[i][j] = 0
                        rows[i].remove(num)
                        cols[j].remove(num)
                        subgrids[get_subgrid_index(i, j)].remove(num)
                return False
    return True

solve()
printMatrix()
