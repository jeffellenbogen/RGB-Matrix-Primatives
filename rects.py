
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
matrix_horizontal = 4 
matrix_vertical = 3

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 

#options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (250,250,250)

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)


while True:
  startRed = random.randint(100,150)
  startGreen = random.randint(0,200)
  startBlue = random.randint(10,255)
  fadeBlue =  random.randint(3,5)
  for i in range (total_rows/2+1):
    #draw.rectangle( (i,i,total_columns-i, total_rows-i), outline = white)
    draw.rectangle( (i,i,total_columns-i,total_rows-i), outline = (startRed,startGreen,startBlue-fadeBlue*i) )
    sleep(.03)
    matrix.SetImage(image, 0, 0)
  
  sleep(1)
  linewidth = random.randint(5,20)
  offset = random.randint(5,40)

  for i in range (linewidth):
    draw.line((i,0,i+offset,96),fill=white)
    draw.line((i+2*linewidth,0,i+2*linewidth+offset,96),fill=red)
    draw.line((i+4*linewidth,0,i+4*linewidth+offset,96),fill=green)
    draw.line((i+6*linewidth,0,i+6*linewidth+offset,96),fill=blue)
    matrix.SetImage(image, 0, 0)
    sleep(.01)
  sleep(1)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

