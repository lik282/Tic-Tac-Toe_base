def display_board(board):
  """
  Should print the tic tac toe board in a format similar to
       1   2   3
    A   X | O | . 
       ---+---+---
    B   X | O | .
       --+---+---
    C   0 | X | . 
       --+---+---
  """


  print("    1   2   3")
  for i, sor in enumerate(board):
        sorszam = chr(ord('A') + i)  # A, B, C sorok
        print(f"  {sorszam}  {sor[0]} | {sor[1]} | {sor[2]}")
        if i < 2:
            print("    ---+---+---")
  pass

display_board()