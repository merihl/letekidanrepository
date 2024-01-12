# Paint cover calculator
import math
cover = 5

def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = math.ceil(area / cover)
  
  print(f"You'll need {num_of_cans} cans of paint.")

heighht = int(input("Height of wall: "))
width = int(input("Width of wall: "))
paint_calc(height=heighht, width=width, cover=cover)
