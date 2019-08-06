
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

radius = 6
rotation = 0
sectors = 8
sectorAngle = 360 / sectors

###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)

while True:

'''
    #animate worm explosion  
  death_color = (255,0,0)
  death_fill = (255,255,255)
  for deathloop in range(3,13,2):
    ellipse_offset = (deathloop-1)/2
    temp_image = Image.new("RGB", (deathloop,deathloop))
    temp_draw = ImageDraw.Draw(temp_image)
    temp_draw.ellipse((0,0,deathloop-1,deathloop-1), outline=death_color, fill=death_fill)
    matrix.SetImage(temp_image, worm[0][0]-ellipse_offset,worm[0][1]-ellipse_offset)
    time.sleep(.1)
'''
  draw.ellipse((0,0,2 * radius, 2 * radius), outline = white, fill=red)
  draw.rectangle((0,0,2 * radius,2 * radius) outline = black, fill=black)
  #rotate a second black rectangle to sectorAngle degrees + rotation degrees based on for loop for spinning effect


# refer to https://stackoverflow.com/questions/34747946/rotating-a-square-in-pil for more info on drawing Polygons with vertices
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

