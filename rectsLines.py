
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


#options.hardware_mapping = 'adafruit-hat-pwm' 
#options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
options.hardware_mapping = 'regular'  

options.gpio_slowdown = 2

matrix = RGBMatrix(options = options)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (250,250,250)
bg_color = (255, 255, 255)

counter = 1

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)

#linewidth = random.randint(5,20)
#offset = random.randint(5,40)


while True:
  xIncrementer = random.randint(2,20)
  yIncrementer = random.randint(2,20)
  
  for y in range (0, total_rows + yIncrementer, yIncrementer):
    randomColor = random.randint(0,360)
    if counter % 2 == 0:
      bg_color ="hsl({}, 100%, 50%)".format(randomColor) 
    else:
      bg_color = (0,0,0)
    for x in range (0, total_columns + xIncrementer, xIncrementer):
       draw.line( (0,y,x,total_rows), fill = bg_color)
       draw.line( (0,total_rows-y,x,0), fill = bg_color)
       draw.line( (total_columns,y,total_columns - x,total_rows), fill = bg_color)
       draw.line( (total_columns,total_rows-y,total_columns - x,0), fill = bg_color)
       sleep(.01)
       matrix.SetImage(image, 0, 0)
    sleep(.01)
  counter+=1  
  
 


 

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

