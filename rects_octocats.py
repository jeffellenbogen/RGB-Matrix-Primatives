
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

#create an instance of the image object to allow for it to be used globally in functions and main loop
temp_image = Image.new("RGB", (total_columns,total_rows))
temp_draw = ImageDraw.Draw(temp_image)

imageSize = 28

###################################
# Background
###################################
def background():
  global temp_image
  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 50%)".format(randomColor)
  temp_draw = ImageDraw.Draw(temp_image)
  temp_draw.rectangle((0,0,total_columns,total_rows), fill= bg_color)
  matrix.SetImage(temp_image,0,0)

###################################
# Image Setup
###################################
def newImage():
  # used global keyword here to access the object image in the main loop
  global temp_image
  global imageSize
  global total_rows
  global total_columns

  pickImage = random.randint(1,4)
  if pickImage == 1:
    local_image = Image.open("./rects_octocats/octocat-Eva256.jpg").convert('RGB')
  elif pickImage == 2:
    local_image = Image.open("./rects_octocats/octocat-Jeff256.jpg").convert('RGB')
  elif pickImage == 3:
    local_image = Image.open("./rects_octocats/octocat-Molly256.jpg").convert('RGB')  
  else:
    local_image = Image.open("./rects_octocats/octocat-Sam256.jpg").convert('RGB')
  local_image = local_image.resize((imageSize,imageSize))
  
  imageOffsetX = (total_columns - imageSize) // 2
  imageOffsetY = (total_rows - imageSize) // 2
  temp_image.paste(local_image, (imageOffsetX,imageOffsetY))
  matrix.SetImage(temp_image,0,0)

###################################
# ScreenWipe
###################################
def ScreenWipe(direction):
  global temp_image
  global temp_draw
  global total_rows
  global total_columns
  wipeSpeed = .03

  randomColor = random.randint(0,360)
  bg_color ="hsl({}, 100%, 50%)".format(randomColor)

  #Vertical wipe
  if (direction == 1): 
    for y in range (total_rows):
      temp_draw.line((0,y,total_columns,y), fill=bg_color)
      matrix.SetImage(temp_image,0,0)
      sleep(wipeSpeed)

  #Horizontal wipe    
  elif (direction == 2):
      for x in range (total_columns):
        temp_draw.line((x,0,x,total_rows), fill=bg_color)
        matrix.SetImage(temp_image,0,0)
        sleep(wipeSpeed)  

  #Diagonal wipe -- This currently doesn't work as desired. See issue #6
  else:
      for z in range (total_rows+total_columns):
        temp_draw.line((0,z,total_columns,z - total_columns), fill=bg_color)
        matrix.SetImage(temp_image,0,0)
        sleep(wipeSpeed/2)    

###################################
# Main loop 
###################################
background()
sleep(2)
while True:
  newImage()
  sleep(2)
  ScreenWipe(random.randint(1,3))
  sleep(1)

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

