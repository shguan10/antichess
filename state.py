import numpy as np

from enum import Enum,auto

CHESS_COLS = "abcdefgh"

class Chess_Pieces(Enum):
  king=auto()
  queen=auto()
  rook = auto()
  bishop = auto()
  knight = auto()
  pawn = auto()

class Chess_Players (Enum):
  white = auto()
  black = auto()

def chess_to_zero_indexed(cpos):
  col=cpos[0]
  row = cpos[1:]

  col = np.argmax(np.array([letter==col for letter in CHESS_COLS]))
  row = int(cpos)
  return (row,col)

def zero_indexed_to_chess(row_col_tuple):
  row,col = row_col_tuple

  cpos0 = CHESS_COLS[col]
  cpos1 = str(row)
  return cpos0+cpos1

class Piece:
  def __init__(self,kind,location,owner):
    # kind is a integer representing which piece it is
    # location is a 0 indexed tuple representing where the piece is at
    # owner is 0 for white, 1 for black
    self.location = location
    self.kind = kind
    self.owner = owner

  def valid_moves(self,board):
    # board is a matrix of None or Piece


    # first the raw valid moves if there were no other pieces on the board, and the board was infinite
    if self.kind is Chess_Pieces.king:
      places = [row,col for row in [-1,0,1] for col in [-1,0,1]]
      places = [row+self.location[0],col+self.location[1] for row,col in places]
    elif self.kind is Chess_Pieces.queen:
      # vertical
      places = [row-7+self.location[0],self.location[1] for row in range(15)]
      # horizontal
      places += [self.location[0],col-7+self.location[1] for col in range(15)]
      # diagonals
      places += [ind-7+self.location[0],ind-7+self.location[1] for ind in range(15)]
      places += [ind-7+self.location[0],-(ind-7)+self.location[1] for ind in range(15)]

    elif self.kind is Chess_Pieces.rook:
      # vertical
      places = [row-7+self.location[0],self.location[1] for row in range(15)]
      # horizontal
      places += [self.location[0],col-7+self.location[1] for col in range(15)]
    elif self.kind is Chess_Pieces.bishop:
      # diagonals
      places = [ind-7+self.location[0],ind-7+self.location[1] for ind in range(15)]
      places += [ind-7+self.location[0],-(ind-7)+self.location[1] for ind in range(15)]

    elif self.kind is Chess_Pieces.knight:
      NEWS = np.array([[r-1,c-1] for r in range(3) for c in range(3)])

      places = [2*news+(np.array([1,1])-news)*lr 
                  for news in NEWS for lr in [-1,1]]
      places = [row+self.location[0],col+self.location[1] for row,col in places]
    
    elif self.kind is Chess_Pieces.pawn:
      places = [(1,0) if self.owner==0 else (-1,0)]

    # filter by those positions on the board
    places = [row,col for row,col in places if 0<=row<8 and 0<=col<8]

    #filter by those positions blocked by your own pieces
    places = [row,col for row,col in places if board[row,col] is None or board[row,col].owner!=self.owner]

    #filter by those positions blocked by enemy pieces
    if self.kind not in [Chess_Pieces.king,Chess_Pieces.knight,Chess_Pieces.pawn]:
      # queen, bishop, rook can be blocked
      

class State:
  # this class contains the current state of the chess board
  def __init__(self):
    self.player = 0 # white to move
    self.
