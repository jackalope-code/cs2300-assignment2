import numpy
from decimal import Decimal, getcontext

class Gameboard:
  def __init__(self, width, height):
    self.board = numpy.full((width, height), '_')
    self.width = width
    self.height = height

  def load_game(self, filename):
    with open('filename', 'r') as f:
      header = f.readline().split(' ')
      size = int(header[0])
      k = int(header[1])
      move_strings = f.readlines()
      print(move_strings)
      # TODO: Use and test values

  def check_play(self, start_row, start_col, dest_row, dest_col):
    if self.board[start_row][start_col] == '_' and \
      self.board[dest_row][dest_col] == '_':
      # Perpendicular check
      pass

  def __str__(self):
    separator = " = " * self.width
    return separator+"\n"+str(self.board)+"\n"+separator;

  # y = (y1-y0)/(x1-x0)x + b
  # (x1-x0)y = (y1-y0)x + (x1-x0)b
  # f(x, y) = (y1-y0)x - (x1-x0)y + (x1-x0)b
  def draw_horizontal_line(self, sx, sy, dx, dy, value):
    x=sx
    y=sy
    (x_dif, y_dif) = slope_deltas(sx, sy, dx, dy)
    f = lambda x, y: y_dif*x -x_dif*y + x_dif*sy
    while True:
      if(x == dx and y == dy or x > len(self.board[0]) or y > len(self.board) or x < 0 or y < 0):
        break;
      self.board[y][x] = value
      if f(x+1, y + 1/2) > 0:
        x += 1
        y += 1
      else:
        x += 1

 # TODO: this is still broken
  def draw_vertical_line(self, sx, sy, dx, dy, value):
    x=sx
    y=sy
    (x_dif, y_dif) = slope_deltas(sx, sy, dx, dy)
    f = lambda x, y: y_dif*x -x_dif*y + x_dif*sy
    while True:
      if(x == dx and y == dy or x >= len(self.board[0]) or y >= len(self.board) or x < 0 or y < 0):
        break;
      self.board[y][x] = value
      print("Setting ({}, {})".format(x, y))
      if f(x+1/2, y + 1) > 0:
        x += 1
        y += 1
      else:
        y += 1

  def draw_line(self, x0, y0, x1, y1):
    (dx, dy) = slope_deltas(x0, y0, x1, y1)
    x = x0
    y = y0
    for i in range(x0, x1+1):
      x += 1
      y += dy

  def draw_stepped_line(self, x0, y0, x1, y1, value, rounding_precision=None):
    (dx, dy) = slope_deltas(x0, y0, x1, y1)
    print(dx, dy)
    x = Decimal(x0)
    y = Decimal(y0)
    if abs(dy) < abs(dx):
      # Iterate along x
      steps = abs(dx)
      x_incr = 1
      y_incr = Decimal(dy/steps)
      if rounding_precision:
        y_incr = y_incr.quantize(Decimal(rounding_precision))
      print("increment", y_incr)
    else:
      # Case of dy > dx, so iterate along y
      steps = abs(dy)
      x_incr = Decimal(dx/steps)
      if rounding_precision:
          x_incr = x_incr.quantize(Decimal(rounding_precision))
      y_incr = 1
      print("increment", x_incr)
    
    for i in range(steps+1):
      print("Plotting {} at ({}, {})".format(str(value), round(x), round(y)))
      self.board[round(y)][round(x)] = value
      x += x_incr
      y += y_incr



  def flip(self):
    return numpy.flip(self.board, axis=0)
  
  def score(self):
    p1_score = 0
    p2_score = 0
    for row in self.board:
      for element in row:
        if element == 'X':
          p1_score += 1
        elif element == 'O':
          p2_score += 1
    return (p1_score, p2_score)

# Returns a tuple with the differences between x and y
def slope_deltas(sx, sy, dx, dy):
  return (dx-sx, dy-sy)

def slope_deltas_pt(p1, p2):
  sx = p1[0]
  sy = p1[1]
  dx = p2[0]
  dy = p2[1]
  return (dx-sx, dy-sy)


# my/(mx) * ny/(nx) = -1
# my*nx * ny*mx = -(mx*nx)
def check_perpendicular(slope1, slope2):
  x1 = slope1[0]
  y1 = slope1[1]
  x2 = slope2[0]
  y2 = slope2[1]

  left_side = y1*x2 * y2*x1
  right_side = -(x1*x2)
  print(right_side)
  print(left_side)

  return left_side == right_side

def row_col_to_pt(row, col):
  return (col, row)