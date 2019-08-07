
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


spinSpeed = .05

sectors = 8
sectorAngle = 360 / sectors

flowersize = 40
numFlowerRows = 2
numFlowerColumns = 2
spacingFlowerRows = total_columns / (numFlowerColumns * 2 + 1) # multiply by 2 and add one to account for flowers and spaces between
spacingFlowerColumns = total_rows / (numFlowerRows * 2 + 1)
print(spacingFlowerRows)
print(spacingFlowerColumns)



###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
#flower = Image.new("RGB", (flowersize, flowersize)
draw = ImageDraw.Draw(image)


while True:
  for k in range (sectors):
    for i in range(spacingFlowerColumns):
      for j in range(spacingFlowerRows):
        if (i % 2 == 1) & (j % 2 == 1):
          draw.pieslice((i*spacingFlowerColumns,j*spacingFlowerRows, i*spacingFlowerColumns + flowersize, j*spacingFlowerRows + flowersize),sectorAngle * k, sectorAngle * (k+1),outline = blue, fill = red)
    matrix.SetImage(image, 0, 0)
    sleep(spinSpeed)
    for i in range(spacingFlowerColumns):
      for j in range(spacingFlowerRows):
        if (i % 2 == 1) & (j % 2 == 1):
          draw.pieslice((i*spacingFlowerColumns,j*spacingFlowerRows, i*spacingFlowerColumns + flowersize, j*spacingFlowerRows + flowersize),sectorAngle * k - 20, sectorAngle * (k+1) + 20,outline = black, fill = black)
    matrix.SetImage(image, 0, 0)


  
  

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

