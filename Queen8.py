def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1
    
    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1
    
    # If no conflicts, the position is safe
    return True

def solve_n_queens_util(board, row, solutions):
    # Base case: all queens are placed
    if row == len(board):
        solutions.append(list(board))
        return
    
    # Try placing queen in each column in current row
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens_util(board, row + 1, solutions)
            board[row] = -1
    
    return

def solve_n_queens():
    board = [-1] * 8
    solutions = []
    solve_n_queens_util(board, 0, solutions)
    
    if solutions:
        for i, solution in enumerate(solutions):
            print("Solution {}: ".format(i+1))
            for row in range(len(solution)):
                line = ""
                for col in range(len(solution)):
                    if solution[row] == col:
                        line += "Q "
                    else:
                        line += ". "
                print(line)
            print("")
    else:
        print("No solution exists.")
solve_n_queens()