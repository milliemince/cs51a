#millie mince
#cs51a
#assignment 9
#november 8 2019

import copy 

class NQueenState:
    """NQueenState takes an input size chess board, generates that board, and is
    able to perform a variety of functions on that board to ultimately return
    the number of valid solutions there are to the NQueens problem given that
    size chess board. It is able to check if a position on the board is a valid
    position for a new queen to be placed (taking into account the existing 
    queens on the board. Once the number of valid queens placed on the board
    is equal to the size of the board, the class recognizes this as a goal state
    and stores it as a solution"""
    
    def __init__(self, size):
        """constructer for NQueenState class. Creates variables size,
        num_queens_placed (initialized at 0), and generates an initial
        board in which there are 0 queens placed"""
        self.size = size
        self.num_queens_placed = 0
        self.board = self.generate_board()
    
    def generate_board(self):
        """generates a blank board"""
        new_board = []
        for i in range(self.size):
            new_board.append(["0"] * self.size)
        return new_board
    
    def __str__(self):
        """returns a string that states the size of the board, the number
        of queens placed, and the current state of the board"""
        #formatting board correctly
        formatted_board = ""
        for i in range(self.size):
            formatted_board += str(self.board[i]) + "\n"
        return "Board size: " + str(self.size) + "\n" + "Number of Queens placed: " + str(self.num_queens_placed) + "\n" + str(formatted_board)
    
    def is_valid_move(self, somerow, somecol):
        """checks if placing a queen in somerow, somecol is a valid move by
        checking if there is already a queen in the place, if there are still
        less than self.size queens placed on the board, and if the queen
        can be attacked by any existing queens on the board"""
        bool_1 = self.board[somerow][somecol] != 1
        bool_2 = self.num_queens_placed < self.size        
        bool_3 = self.attack(somerow, somecol)
        return bool_1 and bool_2 and bool_3
    
    def is_valid_position(self, somerow, somecol):
        """checks if input somerow, somecol is a valid position on the board"""
        valid_row = 0 <= somerow <= (self.size-1)
        valid_col = 0 <= somecol <= (self.size-1)
        #need to use self.size - 1 because while we're thinking of an 8x8 chess board, the computer is thinking of a 0x7 chess board
        return valid_row and valid_col

    def attack(self, somerow, somecol):
        """checks if a queen placed at somerow, somecol can be attacked
        by existing queens on the board. It checks if there are any existing
        queens in the same row, column, or diagonal that the new queen is 
        trying to be placed at"""
        valid_move = True
        for i in range(self.size):
            if self.is_valid_position(somerow, i):
                if self.board[somerow][i] != "0":
                    #checks the same row
                    valid_move = False
        for i in range(self.size):
            if self.is_valid_position(i, somecol):
                if self.board[i][somecol] != "0":
                    #checks the same column
                    valid_move = False 
        for i in range(self.size):
            if self.is_valid_position(somerow+i, somecol+i):
                if self.board[somerow+i][somecol+i] != "0":
                    #checks diagonal
                    valid_move = False
        for i in range(self.size):
            if self.is_valid_position(somerow+i, somecol-i):
                if self.board[somerow+i][somecol-i] != "0":
                    valid_move = False
        for i in range(self.size):
            if self.is_valid_position(somerow-i, somecol+i):
                if self.board[somerow-i][somecol+i] != "0":
                    valid_move = False
        for i in range(self.size):
            if self.is_valid_position(somerow-i, somecol-i):
                if self.board[somerow-i][somecol-i] != "0":
                    valid_move = False
        return valid_move
    
    def add_queen(self, somerow, somecol):
        """updates the board by creating a new board and placing a new queen
        at somerow, somecol. function also adds one to num_queens_placed
        to keep track of the number of valid queens that have been placed
        on the board"""
        if self.is_valid_move(somerow, somecol):
            new_state = copy.deepcopy(self.board)
            new_state[somerow][somecol] = 1
            self.num_queens_placed += 1
            self.board = new_state 
        
    def next_states(self):
        """returns the next possible states by checking each position in the 
        row after the one where the last queen was placed. if a position in
        the following row is a valid position, then it adds that state to 
        the list of next_states. the function returns the list of the next 
        states"""
        possible_col = []
        for i in range(self.size):
            if self.is_valid_move(self.num_queens_placed, i):
                possible_col.append(i)
        next_states = []
        for column in possible_col:
            next_state = copy.deepcopy(self)
            next_state.add_queen(self.num_queens_placed, column)
            next_states.append(next_state)
        return next_states
    
    def is_goal(self):
        return self.num_queens_placed == self.size
                

def dfs(state):
    """Recursive depth first search implementation
    
    Input:
    Takes as input a state.  The state class MUST have the following
    returned True) that can be reached from the input state.
    """

    #if the current state is a goal state, then return it in a list
    if state.is_goal():
        return [state]
    else:
        # else, recurse on the possible next states
        result = []
        
        for s in state.next_states():
            # append all of the s
            result += dfs(s)
            
        return result
    
# uncomment this code when you're ready to test it out
start_state = NQueenState(8)


solutions = dfs(start_state)
print("There were " + str(len(solutions)) + " solutions.\n")

if( len(solutions) > 0 ):
    print(solutions[0])
    
    