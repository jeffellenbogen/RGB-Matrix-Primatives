# Used in main loop
from time import sleep
import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont


fntLG = ImageFont.truetype('Pillow/Tests/fonts/times.ttf', 18)
fntSM = ImageFont.truetype('Pillow/Tests/fonts/arial.ttf', 14)

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


#speed = .05
pause = .2

image = Image.new("RGB", (total_columns,total_rows))
drawRect = ImageDraw.Draw(image)
drawText = ImageDraw.Draw(image)

colorInc = 0
white = (255,255,255)

while True:
  width = random.randint(2, total_columns//2)
  height = random.randint (2,total_rows//2)
  xCoord = random.randint (0,total_columns)
  yCoord = random.randint (0,total_rows)
  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 50%)".format(randomColor) 
  randomColor = random.randint(0,360) 
  fill_color = "hsl({}, 100%, 20%)".format(randomColor)  
  drawRect.rectangle( (xCoord,yCoord,width,height), outline = bg_color, fill = fill_color) 
  colorInc+=5
  if colorInc > 360:
    colorInc = 0
  
  white = (255,255,255)
  black = (0,0,0)
  #text_color = "hsl({}, 100%, 50%)".format(colorInc)  
  text_color = white  
  drawText.multiline_text((0,20),"TECHNOLOGY\nIS COOL!",font = fntLG, fill = text_color, align = "center", spacing = 10)
  #drawText.text((5,5), "TECHNOLOGY", font = fntSM, fill=text_color)
  #drawText.text((14,35), "IS COOL!", font = fntLG, fill=text_color) 
  matrix.SetImage(image, 0, 0)    
  sleep(pause)



