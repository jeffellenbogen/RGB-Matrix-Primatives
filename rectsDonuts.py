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
black = (0,0,0)

xCenterPt = random.randint(0,total_columns)
yCenterPt = random.randint(0,total_rows)
donutSize = random.randint(6,60)

speed = .05
pause = 1

image = Image.new("RGB", (total_columns,total_rows))
drawRect = ImageDraw.Draw(image)
drawCircle = ImageDraw.Draw(image)
drawPoint = ImageDraw.Draw(image)

while True:
  xCenterPt = random.randint(0,total_columns)
  yCenterPt = random.randint(0,total_rows)
  donutSize = random.randint(6,60)
  
  drawPoint.point((xCenterPt,yCenterPt), fill = blue)
  for i in range (donutSize/2):
    
    drawCircle.ellipse((xCenterPt - i, yCenterPt - i, xCenterPt + i, yCenterPt + i), outline = blue )
  for i in range (donutSize/2,donutSize):
    drawCircle.ellipse((xCenterPt - i, yCenterPt - i, xCenterPt + i, yCenterPt + i), outline = red )
  matrix.SetImage(image, 0, 0)

  sleep(pause)    


