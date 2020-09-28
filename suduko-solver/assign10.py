# millie mince and graham hirsch
# cs51a
# assignment 10
# 11/20/19
# creating and solving a sudoku board

import copy
import time

class SudokuState:
    """
    this class constructs a 9 by 9 starting sudoku board, 
    continuously adding numbers to a new state and checking to see if 
    that new number can be placed in that place. the program does 
    this by checking the row and column, making sure that the number 
    isn't the same.
    """
    def __init__(self):
        """
        this function constructs the 9 by 9 matrix for the sudoku board
        """
        self.size = 9
        self.num_placed = 0
        self.board = []
        
        for i in range (self.size):
            mid_list = []
            for i in range (self.size):
                mid_list.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            self.board.append(mid_list)
        
    def is_filled(self, somerow, somecol):
        """
        function checks to see if the current space in a row or 
        column is filled
        """
        position = self.board[somerow][somecol]
        return isinstance(position, int)
    
    def remove_conflict(self, somerow, somecol, somenum):
        """
        removes somenum from self.board[somerow][somecol]
        """
        if not self.is_filled(somerow, somecol):
            if somenum in self.board[somerow][somecol]:
                self.board[somerow][somecol].remove(somenum)
            
    def remove_all_conflicts(self, somerow, somecol, somenum):
        """
        removes the possibility of a number being filled into an 
        empty space if it already appears in that same row, column, 
        or subgrid
        """
        sub_grid_placement = self.get_subgrid_number(somerow, somecol)
        for i in range(9):
            self.remove_conflict(somerow, i, somenum)
            self.remove_conflict(i, somecol, somenum)
        for r in range(9):
            for c in range(9):
                if self.get_subgrid_number(r, c) == sub_grid_placement:
                    self.remove_conflict(r, c, somenum)
            
    def add_number(self, somerow, somecol, somenum):
        """
        creates a new sudoku board with somenum added into somerow 
        and somcol
        """
        new_state = copy.deepcopy(self)
        new_state.board[somerow][somecol] = somenum
        new_state.remove_all_conflicts(somerow, somecol, somenum)
        new_state.num_placed += 1
        return new_state
        
    def get_most_constrainted_cell(self):
        """
        finds the row and column with the fewest possible options 
        remaining
        """
        most_constrainted_cell_length = 9
        constrainted_cell_row = 0
        constrainted_cell_column = 0
        for row in range(9):
            for column in range(9):
                if not self.is_filled(row, column):
                    if len(self.board[row][column]) < most_constrainted_cell_length:
                        most_constrainted_cell_length = len(self.board[row][column])
                        constrainted_cell_row = row
                        constrainted_cell_column = column
        return (constrainted_cell_row, constrainted_cell_column)
    
    def solution_is_possible(self):
        """
        continues to solve the sudoku board until every single space 
        has only one possible solution left, otherwise this function 
        returns False and the program continues to run
        """
        possible = True
        for i in range(9):
            for i in range(9):
                if self.board[i][i] == []:
                    possible = False
        return possible
        
    def next_states(self):
        """
        works with get_most_constrained_cell to solve the sudoku 
        board in the fastest way possible by creating a next state 
        everytime a number is put into the most contrained cell
        """
        next_states = []
        most_constrainted_cell = self.get_most_constrainted_cell()
        row = most_constrainted_cell[0]
        col = most_constrainted_cell[1]
        if not self.is_filled(row, col):
            for num in self.board[row][col]:
                possible_state = self.add_number(row, col, num)
                if possible_state.solution_is_possible():
                    next_states.append(possible_state)
        return next_states
    
    def is_goal(self):
        """
        finishes the program when all 81 numbers are placed into the 
        board
        """
        return self.num_placed == 81
    
    def get_subgrid_number(self, row, col):
        """
        Returns a number between 1 and 9 representing the subgrid
        that this row, col is in.  The top left subgrid is 1, then
        2 to the right, then 3 in the upper right, etc.
        """
        row_q = int(row/3)
        col_q = int(col/3)
        return row_q * 3 + col_q + 1
    
    def get_any_available_cell(self):
        """
        An uninformed cell finding variant.  If you use
        this instead of find_most_constrained_cell
        the search will perform a depth first search.
        """
        for r in range(self.size):
            for c in range(self.size):
                if not self.is_filled(r,c):                    
                    return (r, c)
    
    def get_raw_string(self):
        board_str = ""
  
        for r in self.board:
            board_str += str(r) + "\n"
      
        return "num placed: " + str(self.num_placed) + "\n" + board_str
      
    def __str__(self):
        """
        prints all numbers assigned to cells.  Unassigned cells (i.e.
        those with a list of options remaining are printed as blanks
        """
        board_string = ""
        
        for r in range(self.size):
            if r % 3 == 0:
                board_string += " " + "-" * (self.size * 2 + 5) + "\n"
      
            for c in range(self.size):
                entry = self.board[r][c]
        
                if c % 3 == 0:
                    board_string += "| "    
            
                if isinstance(entry, list):
                    board_string += "_ "
                else:
                    board_string += str(entry) + " "
                
            board_string += "|\n"
      
        board_string += " " + "-" * (self.size * 2 + 5) + "\n" 
        
        return "num placed: " + str(self.num_placed) + "\n" + board_string    


# -----------------------------------------------------------------------
# Make all of your changes to the SudokuState class above.
# only when you're running the last experiments will
# you need to change anything below here and then only
# the different problem inputs

# -----------------------------------
# Even though this is the same DFS code
# that we used last time, our next_states
# function is makeing an "informed" decision
# so this algorithm performs similarly to
# best first search.
def dfs(state):
    """
    Recursive depth first search implementation
  
    Input:
    Takes as input a state.  The state class MUST have the following
    methods implemented:
    - is_goal(): returns True if the state is a goal state, False otherwise
    - next_states(): returns a list of the VALID states that can be
    reached from the current state
    
    Output:
    Returns a list of ALL states that are solutions (i.e. is_goal
    returned True) that can be reached from the input state.
    """    
    #if the current state is a goal state, then return it in a list
    if state.is_goal():
        return [state]
    else:
        #make a list to accumulate the solutions in
        result = []
  
        for s in state.next_states():
            result += dfs(s)
      
        return result

# ------------------------------------
# three different board configurations:
# - problem1
# - problem2
# - heart (example from class notes)
def problem1():
    b = SudokuState()
    b = b.add_number(0, 1, 7)
    b = b.add_number(0, 7, 1)
    b = b.add_number(1, 2, 9)
    b = b.add_number(1, 3, 7)
    b = b.add_number(1, 5, 4)
    b = b.add_number(1, 6, 2)
    b = b.add_number(2, 2, 8)
    b = b.add_number(2, 3, 9)
    b = b.add_number(2, 6, 3)
    b = b.add_number(3, 1, 4)
    b = b.add_number(3, 2, 3)
    b = b.add_number(3, 4, 6)
    b = b.add_number(4, 1, 9)
    b = b.add_number(4, 3, 1)
    b = b.add_number(4, 5, 8)
    b = b.add_number(4, 7, 7)
    b = b.add_number(5, 4, 2)
    b = b.add_number(5, 6, 1)
    b = b.add_number(5, 7, 5)
    b = b.add_number(6, 2, 4)
    b = b.add_number(6, 5, 5)
    b = b.add_number(6, 6, 7)
    b = b.add_number(7, 2, 7)
    b = b.add_number(7, 3, 4)
    b = b.add_number(7, 5, 1)
    b = b.add_number(7, 6, 9)
    b = b.add_number(8, 1, 3)
    b = b.add_number(8, 7, 8)
    return b
    
def problem2():
    b = SudokuState()
    b = b.add_number(0, 1, 2) 
    b = b.add_number(0, 3, 3) 
    b = b.add_number(0, 5, 5)
    b = b.add_number(0, 7, 4)
    b = b.add_number(1, 6, 9)
    b = b.add_number(2, 1, 7)
    b = b.add_number(2, 4, 4)
    b = b.add_number(2, 7, 8)
    b = b.add_number(3, 0, 1)
    b = b.add_number(3, 2, 7)
    b = b.add_number(3, 5, 9)
    b = b.add_number(3, 8, 2)
    b = b.add_number(4, 1, 9)
    b = b.add_number(4, 4, 3)
    b = b.add_number(4, 7, 6)
    b = b.add_number(5, 0, 6)
    b = b.add_number(5, 3, 7)
    b = b.add_number(5, 6, 5)
    b = b.add_number(5, 8, 8)
    b = b.add_number(6, 1, 1)
    b = b.add_number(6, 4, 9)
    b = b.add_number(6, 7, 2)
    b = b.add_number(7, 2, 6)
    b = b.add_number(8, 1, 4)
    b = b.add_number(8, 3, 8)
    b = b.add_number(8, 5, 7)
    b = b.add_number(8, 7, 5)
    return b

def heart():
    b = SudokuState()
    b = b.add_number(1, 1, 4)
    b = b.add_number(1, 2, 3)
    b = b.add_number(1, 6, 6)
    b = b.add_number(1, 7, 7)
    b = b.add_number(2, 0, 5)
    b = b.add_number(2, 3, 4)
    b = b.add_number(2, 5, 2)
    b = b.add_number(2, 8, 8)
    b = b.add_number(3, 0, 8)
    b = b.add_number(3, 4, 6)
    b = b.add_number(3, 8, 1)
    b = b.add_number(4, 0, 2)
    b = b.add_number(4, 8, 5)
    b = b.add_number(5, 1, 5)
    b = b.add_number(5, 7, 4)
    b = b.add_number(6, 2, 6)
    b = b.add_number(6, 6, 7)
    b = b.add_number(7, 3, 5)
    b = b.add_number(7, 5, 1)
    b = b.add_number(8, 4, 8)
    return b


# --------------------------------
# Code that actual runs a sudoku problem, times it
# and prints out the solution.
# You can vary which problem your running on between 
# problem1(), problem2() and heart() by changing the line
# below
#
# Uncomment this code when you have everything implemented and you
# want to solve some of the sample problems!

problem = problem1()
print("Starting board:")
print(problem)

start_time = time.time()
solutions = dfs(problem)
search_time = time.time()-start_time

print("Search took " + str(round(search_time, 2)) + " seconds")
print("There was " + str(len(solutions)) + " solution.\n\n")
if len(solutions) > 0:
    print(solutions[0])
