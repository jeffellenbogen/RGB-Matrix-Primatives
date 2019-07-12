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
matrix_horizontal = 2
matrix_vertical = 1

total_rows = matrix_rows * matrix_vertical
total_columns = matrix_columns * matrix_horizontal

options = RGBMatrixOptions()
options.rows = matrix_rows 
options.cols = matrix_columns 
options.chain_length = matrix_horizontal
options.parallel = matrix_vertical 

options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
#options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)

randomColor = random.randint(0,360)
bg_color ="hsl({}, 100%, 20%)".format(randomColor)

image = Image.new("RGB", (total_columns,total_rows))
drawRect = ImageDraw.Draw(image)
drawCircle = ImageDraw.Draw(image)

for i in range (total_rows/2+1):
  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)
  drawRect.rectangle( (i,i,total_columns-i,total_rows-i), outline = bg_color ) 
  sleep(.03)
  matrix.SetImage(image, 0, 0)
  
sleep(1)

for i in range (total_rows/2+1):
  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)
  drawCircle.ellipse(( i + (total_columns - total_rows), i,total_rows-i, total_rows-i), outline = bg_color )
  sleep(.03)
  matrix.SetImage(image, 0, 0)

sleep(1)    

for i in range (total_rows/2+1):
  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)
  drawRect.rectangle( (i,i,total_columns-i,total_rows-i), outline = bg_color )
  sleep(.03)
  matrix.SetImage(image, 0, 0)
  
sleep(1)
