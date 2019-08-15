
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

xCenterPt = total_columns/2 - 1
yCenterPt = total_rows/2 - 1
incrementer = 4

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)


while True:
  for i in range (0, total_rows/2, incrementer):
    draw.rectangle((xCenterPt - i,yCenterPt - i,xCenterPt + i,yCenterPt + i), outline = (red))
    sleep(.05)
    matrix.SetImage(image, 0, 0)
    draw.ellipse((xCenterPt- i - incrementer/2,yCenterPt - i - incrementer/2,xCenterPt + i + incrementer/2,yCenterPt + i + incrementer/2), outline = (blue))
    sleep(.05)
    matrix.SetImage(image, 0, 0)  
  sleep(1)


try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)
