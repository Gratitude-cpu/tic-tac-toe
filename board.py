class Board:
        def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
        def get_size(self): 
            return len(self.board)
             # optional, return the board size (an instance size)
        def get_winner(self):
             return(self.winner)
            # return the winner's sign O or X (an instance winner)     
        def set(self, cell, sign):
             values = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
             codes = (0,1,2, 3,4,5,6,7,8)
             for i in range(len(values)):
                if cell == values[i]:
                    return codes[values.index(cell)]

            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you 
        def isempty(self, cell):
             values = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3']
             codes = (0, 1, 2, 3,4, 5, 6, 7,8)
             for i in range(len(values)):
               if cell == values[i]:
                    cell1 = codes[i]
                    if self.board[cell1] == " ":
                         return(True)
             return False


            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
        def isdone(self):
            done = False
            self.winner = ''

            if (self.board[0] == self.board[1] == self.board[2]) or (self.board[0] == self.board[3] == self.board[6]) or (self.board[0] == self.board[4] == self.board[8]):
                 if self.board[0] == "O":
                      self.winner = "O"
                      done = True
                 elif self.board[0] == "X":
                      self.winner = "X"
                      done = True
            elif (self.board[8] == self.board[5] == self.board[2]) or (self.board[8] == self.board[7] == self.board[6]):
                 if self.board[8] == "O":
                      self.winner = "O"
                      done = True
                 elif self.board[8] == "X":
                      self.winner = "X"
                      done = True
            elif (self.board[1] == self.board[4] == self.board[7]) or (self.board[3] == self.board[4] == self.board[5]) or (self.board[4] == self.board[6] == self.board[2]):
                 if self.board[4] == "O":
                      self.winner = "O"
                      done = True
                 elif self.board[4] == "X":
                      self.winner = "X"
                      done = True
            else:
                #  ipdb.set_trace()
                 if " " not in self.board:
                      done = True

            # check all game terminating conditions, if one of them is present, assign the variable done to True
            # depending on conditions assign the instance var winner to O or X
            return done
        def show(self):          
            print("   " + "A" + "   " + "B" + "   " + "C" + "  ")
            print(" +---+---+---+")
            print("1" + "|" + " " + self.board[0] + " " + "|" + " " + self.board[1] +
                                " " + "|" + " " + self.board[2] + " " + "|")
            print(" +---+---+---+")
            print("2" + "|" + " " + self.board[3] + " " + "|" + " " + self.board[4] +
                                " " + "|" + " " + self.board[5] + " " + "|")
            print(" +---+---+---+")
            print("3" + "|" + " " + self.board[6] + " " + "|" + " " + self.board[7] +
                                " " + "|" + " " + self.board[8] + " " + "|")
            print(" +---+---+---+")
            
            
                      
                      