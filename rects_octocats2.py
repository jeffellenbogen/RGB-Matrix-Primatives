
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
#bg_color = (25,25,25)
randomColor = random.randint(0,360)
bg_color ="hsl({}, 100%, 20%)".format(randomColor)

image = Image.new("RGB", (total_columns,total_rows))
draw = ImageDraw.Draw(image)

image = Image.open("./rects_octocats/octocat-Eva256.jpg").convert('RGB')
image = image.resize((80,80))
matrix.SetImage(image,24,8)


###################################
# Background
###################################
def background():
  global bg_color
  global randomColor
  global draw
  global image

  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)
  #temp_image = Image.new("RGB", (total_columns,total_rows))
  #temp_draw = ImageDraw.Draw(temp_image)
  draw.rectangle((0,0,128,96), fill= (255,255,255))
  matrix.SetImage(image,0,0)


###################################
# Image Setup
###################################
def newImage():
  # used global keyword here to access the object image in the main loop
  global image

  pickImage = random.randint(1,4)
  if pickImage == 1:
    image = Image.open("./rects_octocats/octocat-Eva256.jpg").convert('RGB')
  elif pickImage == 2:
    image = Image.open("./rects_octocats/octocat-Jeff256.jpg").convert('RGB')
  elif pickImage == 3:
    image = Image.open("./rects_octocats/octocat-Molly256.jpg").convert('RGB')  
  else:
    image = Image.open("./rects_octocats/octocat-Sam256.jpg").convert('RGB')
  image = image.resize((80,80))

###################################
# ScreenWipe
###################################
def ScreenWipe(direction):
  global image
  global draw
  global total_rows
  global total_columns

  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 20%)".format(randomColor)

  #Vertical wipe
  if (direction == 1): 
    for y in range (96):
      draw.line((0,y,128,y), fill=bg_color)
      matrix.SetImage(image,0,0)
      sleep(.005)

  #Horizontal wipe    
  elif (direction == 2):
      for x in range (128):
        draw.line((x,0,x,96), fill=bg_color)
        matrix.SetImage(image,0,0)
        sleep(.003)  

  #Diagonal wipe -- This currently doesn't work as desired. See issue #6
  else:
      for z in range (225):
        draw.line((0,z,128,z-128), fill=bg_color)
        matrix.SetImage(image,0,0)
        sleep(.001)    

###################################
# Main loop 
###################################
background()

while True:
  matrix.SetImage(image,24,8)
  sleep(3)
  ScreenWipe(random.randint(1,3))
  newImage()

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

