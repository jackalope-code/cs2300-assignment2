
import numpy as np
from Gameboard import Gameboard, row_col_to_pt
from Gameboard import check_perpendicular, slope_deltas_pt

def test():
  board = Gameboard(16, 16)
  play1 = [(0, 2), (6, 2)]
  play2 = [(4, 0), (3, 5)]
  slope1 = slope_deltas_pt(row_col_to_pt(play1[0][0], play1[0][1]), \
    row_col_to_pt(play1[1][0], play1[1][1]))
  slope2 = slope_deltas_pt(row_col_to_pt(play2[0][0], play2[0][1]), \
    row_col_to_pt(play2[1][0], play2[1][1]))
  print(slope1)
  print(slope2)
  print(check_perpendicular(slope1, slope2))
  print(board);
  # board.draw_stepped_line(2, 8, 8, 2, 'O')
  board.draw_stepped_line(5, 4, 12, 7, 'X')
  board.draw_stepped_line(5, 7, 10, 15, 'O', rounding_precision="0.0000000001")
  board.draw_stepped_line(3, 2, 11, 2, 'O')
  board.draw_stepped_line(2, 4, 2, 12, 'O')
  # board.draw_stepped_line(1, 6, 7, 1, 'O')
  print(board.flip());
  print(board.score())

def main():
    test()

if __name__=="__main__":
    main()