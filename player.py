from random import choice
from board import Board
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            return self.sign
            # return an instance sign
      def get_name(self):
            return self.name
            # return an instance name
      def choose(self, board):
            while True: 
                  cell = input(self.name +',' + self.sign + ': '+ "Enter a cell [A-C][1-3]:")
                  cell = cell.lower()
                  if board.isempty(cell):
                        board.board[board.set(cell,self.sign)] = self.sign
                        break
                  else:
                        #print(cell)
                        print("You did not choose correctly")

                        

class AI(Player):
      def __init__(self, name, sign, board=None):
            self.name = name
            self.sign = sign
            self.moves = self._moves(board)
      def _moves(self, board=None):
            cells = ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]
            return cells
      
      def choose(self, board=None):
            print(f"{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ", end="")
            cell = choice(self.moves)
            cell = cell.lower()
            while not board.isempty(cell):
                  cell = choice(self.moves)
                  cell = cell.lower()
                  
            board.board[board.set(cell,self.sign)] = self.sign
            self.moves.remove(cell)

            print(cell)
            print(self.moves)

            #
            #(board.set(cell, self.sign))
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)

class MiniMax(AI):
     def __init__(self, name, sign, board):
        self.name = name
        self.sign = sign
        self.board = board
        self.opponent_sign = ""
        if self.sign == "O":
             self.opponent_sign= "X"
        else:
            self.opponent_sign = "O"

     def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self, board, True, True)
        print(cell)
        board.board[board.set(cell,self.sign)] = self.sign

     def minimax(self, board, self_player, start):
           # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == "":
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
        else:
            move_options = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
            move = ''
            max_score = -100
            score = 0
            min_score = 100
            for cell in move_options:
                if board.isempty(cell):
                    # call minimax recursively
                    if self_player:
                        board.board[board.set(cell,self.sign)] = self.sign
                        score = MiniMax.minimax(self, board, False, False)
                        if score > max_score:
                            max_score = score
                            move = cell

                    else:
                        board.board[board.set(cell,self.opponent_sign)] = self.opponent_sign
                        score = MiniMax.minimax(self, board, True, False)
                        move = cell
                        if score < min_score:
                            min_score = score
                            move = cell
                    board.board[board.set(cell,' ')] = ' '
            if start:
                return move
            elif self_player:
                return max_score
            else:
                return min_score
            

     
             