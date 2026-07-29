import random
from typing import List, Tuple, Set


class Minesweeper:
    def __init__(self, rows: int = 8, cols: int = 8, mines: int = 10):
        """Initialize the minesweeper game."""
        self.rows = rows
        self.cols = cols
        self.mines_count = mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.won = False
        self._place_mines()
        self._calculate_numbers()

    def _place_mines(self):
        """Randomly place mines on the board."""
        mines_placed = 0
        while mines_placed < self.mines_count:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if self.board[row][col] != -1:
                self.board[row][col] = -1
                mines_placed += 1

    def _calculate_numbers(self):
        """Calculate the number of adjacent mines for each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != -1:
                    count = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue
                            nr, nc = row + dr, col + dc
                            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                                if self.board[nr][nc] == -1:
                                    count += 1
                    self.board[row][col] = count

    def reveal(self, row: int, col: int) -> bool:
        """Reveal a cell. Returns False if a mine is hit."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return True
        
        if self.flagged[row][col]:
            return True
        
        if self.revealed[row][col]:
            return True
        
        self.revealed[row][col] = True
        
        # Hit a mine
        if self.board[row][col] == -1:
            self.game_over = True
            return False
        
        # If no adjacent mines, reveal neighbors
        if self.board[row][col] == 0:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if not self.revealed[nr][nc]:
                            self.reveal(nr, nc)
        
        return True

    def toggle_flag(self, row: int, col: int):
        """Toggle a flag on a cell."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return
        
        if not self.revealed[row][col]:
            self.flagged[row][col] = not self.flagged[row][col]

    def check_win(self) -> bool:
        """Check if the game is won."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != -1 and not self.revealed[row][col]:
                    return False
        self.won = True
        return True

    def display(self):
        """Display the game board."""
        print("\n   ", end="")
        for col in range(self.cols):
            print(f" {col}", end="")
        print()
        
        for row in range(self.rows):
            print(f"{row:2} ", end="")
            for col in range(self.cols):
                if self.flagged[row][col]:
                    print(" F", end="")
                elif not self.revealed[row][col]:
                    print(" .", end="")
                elif self.board[row][col] == -1:
                    print(" *", end="")
                elif self.board[row][col] == 0:
                    print("  ", end="")
                else:
                    print(f" {self.board[row][col]}", end="")
            print()
        print()

    def display_solution(self):
        """Display the full board with all mines revealed."""
        print("\n   ", end="")
        for col in range(self.cols):
            print(f" {col}", end="")
        print()
        
        for row in range(self.rows):
            print(f"{row:2} ", end="")
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    print(" *", end="")
                elif self.board[row][col] == 0:
                    print("  ", end="")
                else:
                    print(f" {self.board[row][col]}", end="")
            print()
        print()


def play():
    """Main game loop."""
    print("=" * 40)
    print("WELCOME TO MINESWEEPER")
    print("=" * 40)
    
    # Get game settings
    try:
        rows = int(input("Enter number of rows (default 8): ") or "8")
        cols = int(input("Enter number of columns (default 8): ") or "8")
        mines = int(input("Enter number of mines (default 10): ") or "10")
        
        if mines >= rows * cols:
            print("Too many mines! Adjusting...")
            mines = (rows * cols) // 2
    except ValueError:
        rows, cols, mines = 8, 8, 10
    
    game = Minesweeper(rows, cols, mines)
    moves = 0
    
    print("\nCommands:")
    print("  reveal <row> <col>  - Reveal a cell")
    print("  flag <row> <col>    - Flag/unflag a cell")
    print("  quit                - Quit the game")
    print()
    
    while not game.game_over and not game.won:
        game.display()
        print(f"Moves: {moves} | Flags: {sum(sum(row) for row in game.flagged)} | Mines: {game.mines_count}")
        
        command = input("Enter command: ").strip().lower().split()
        
        if not command:
            continue
        
        if command[0] == "quit":
            print("Game over!")
            game.display_solution()
            break
        
        try:
            if command[0] == "reveal" and len(command) == 3:
                row, col = int(command[1]), int(command[2])
                if not game.reveal(row, col):
                    game.display()
                    print("💥 GAME OVER! You hit a mine!")
                    game.display_solution()
                else:
                    moves += 1
                    if game.check_win():
                        game.display()
                        print(f"🎉 YOU WON! Completed in {moves} moves!")
            
            elif command[0] == "flag" and len(command) == 3:
                row, col = int(command[1]), int(command[2])
                game.toggle_flag(row, col)
            
            else:
                print("Invalid command. Use 'reveal <row> <col>' or 'flag <row> <col>'")
        
        except (ValueError, IndexError):
            print("Invalid input. Please use proper format.")
    
    # Play again option
    if input("\nPlay again? (y/n): ").lower() == "y":
        play()


if __name__ == "__main__":
    play()
