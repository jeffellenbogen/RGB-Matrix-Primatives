
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

imageSize = 50

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


###########################
#create an instance of the image object to allow for it to be used globally in functions and main loop
###########################
image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)

###################################
# Background fill with random color
###################################
randomColor = random.randint(0,360)
bg_color ="hsl({}, 100%, 20%)".format(randomColor)
draw.rectangle((0,0,total_columns,total_rows), fill= bg_color)
matrix.SetImage(image,0,0)
sleep(1)


###################################
# Main loop 
###################################
while True:
  pickImage = random.randint(1,4)
  if pickImage == 1:
    image = Image.open("./rects_octocats/octocat-Eva256.jpg").convert('RGB')
  elif pickImage == 2:
    image = Image.open("./rects_octocats/octocat-Jeff256.jpg").convert('RGB')
  elif pickImage == 3:
    image = Image.open("./rects_octocats/octocat-Molly256.jpg").convert('RGB')  
  else:
    image = Image.open("./rects_octocats/octocat-Sam256.jpg").convert('RGB')
  #image = image.resize((imageSize, imageSize))
  matrix.SetImage(image,(total_columns - imageSize)/2,(total_rows - imageSize)/2)
  sleep(3)

  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)
  direction = random.randint(1,3)
  #Vertical wipe
  if (direction == 1): 
    for y in range (total_rows):
      draw.line((0,y,total_columns,y), fill=bg_color)
      matrix.SetImage(image, 0, 0)
      sleep(.005)
  #Horizontal wipe    
  elif (direction == 2):
    for x in range (total_columns):
      draw.line((x,0,x,total_rows), fill=bg_color)
      matrix.SetImage(image, 0, 0)
      sleep(.003)  
  #Diagonal wipe 
  else:
    for z in range (total_columns+total_rows):
      draw.line((0,z,total_columns,z - total_columns), fill=bg_color)
      matrix.SetImage(image, 0, 0)
      sleep(.001) 
  sleep(1)    

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

