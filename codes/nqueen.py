def solve_n_queens(n):
    # Track which columns, positive diagonals, and negative diagonals are occupied
    occupied_columns = set()
    occupied_pos_diagonals = set()  # Positive diagonals (r + c)
    occupied_neg_diagonals = set()  # Negative diagonals (r - c)
    
    # Store solutions
    solutions = []
    
    # Initialize the board with '.' indicating empty cells
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        # If all rows are filled, add the current board configuration to solutions
        if row == n:
            solution_copy = [" ".join(row) for row in board]
            solutions.append(solution_copy)
            return
        
        # Attempt to place a queen in each column of the current row
        for col in range(n):
            # Check if this position is attacked by any previously placed queen
            if (col in occupied_columns or
                (row + col) in occupied_pos_diagonals or
                (row - col) in occupied_neg_diagonals):
                continue  # Skip this position if it's under attack
            
            # Place a queen and mark the row, column, and diagonals as occupied
            occupied_columns.add(col)
            occupied_pos_diagonals.add(row + col)
            occupied_neg_diagonals.add(row - col)
            board[row][col] = "Q"
            
            # Recursively attempt to place queens in the next row
            backtrack(row + 1)
            
            # Backtrack: remove the queen and unmark the column and diagonals
            occupied_columns.remove(col)
            occupied_pos_diagonals.remove(row + col)
            occupied_neg_diagonals.remove(row - col)
            board[row][col] = "."

    # Start the backtracking process from the first row
    backtrack(0)

    # Print the total number of solutions and each solution board
    if solutions:
        print(f"Total solutions: {len(solutions)}")
        for solution in solutions:
            for row in solution:
                print(row)
            print()
    else:
        print("No solutions.")

# Run the function with n = 8 to solve the 8-queens problem
if __name__ == "__main__":
    solve_n_queens(8)
