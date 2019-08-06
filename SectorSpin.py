
# Used in main loop
from time import sleep
import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

# this is the size of ONE of our matrixes. 
matrix_rows = 32 
matrix_columns = 32 

# how many matrixes stacked horizontally and vertically 
matrix_horizontal = 5 
matrix_vertical = 3

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 


'''options.hardware_mapping = 'adafruit-hat-pwm' 
'''
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (250,250,250)
black = (0,0,0)

flowersize = 20
radius = 6
rotation = 0
sectors = 8
sectorAngle = 360 / sectors

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
flower = Image.new("RGB", (flowersize, flowersize)
draw = ImageDraw.Draw(image)

while True:
  
  draw.pieslice((20,20, 60, 60),345,15,outline = blue, fill = red)
  #rotate a second black rectangle to sectorAngle degrees + rotation degrees based on for loop for spinning effect
  # refer to https://stackoverflow.com/questions/34747946/rotating-a-square-in-pil for more info on drawing Polygons with vertices
  sleep(.03)
  matrix.SetImage(image, 0, 0)


try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

