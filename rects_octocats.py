
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
bg_color = (100,100,100)



#create an instance of the image object to allow for it to be used globally in functions and main loop
image = Image.open("./rects_octocats/octocat-Eva256.jpg").convert('RGB')
image = image.resize((80,80))

###################################
# Background
###################################
def background():
  temp_image = Image.new("RGB", (96,128))
  temp_draw = ImageDraw.Draw(temp_image)
  temp_draw.rectangle((0,0,95,127), fill= (bg_color))
  matrix.SetImage(temp_image,0,0)


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
  #Vertical wipe
  if (direction == 1): 
    for y in range (95):
      temp_image = Image.new("RGB", (128, 1))
      temp_draw = ImageDraw.Draw(temp_image)
      temp_draw.rectangle((0,0,127,0), fill=(bg_color))
      matrix.SetImage(temp_image, 0, y)
      sleep(.01)
  #Horizontal wipe    
  elif (direction == 2):
      for x in range (127):
        temp_image = Image.new("RGB", (1, 95))
        temp_draw = ImageDraw.Draw(temp_image)
        temp_draw.rectangle((0,0,0,95), fill=(bg_color))
        matrix.SetImage(temp_image, x, 0)
        sleep(.01)  
  #Diagonal wipe -- This currently doesn't work as desired. See issue #6
  else:
      for z in range (127):
        temp_image = Image.new("RGB", (z, z))
        temp_draw = ImageDraw.Draw(temp_image)
        temp_draw.rectangle((0,0,z,z), fill=(bg_color))
        matrix.SetImage(temp_image, 0, 0)
        sleep(.01)    

###################################
# Main loop 
###################################
background()
while True:
  matrix.SetImage(image,16,8)
  sleep(3)
  ScreenWipe(random.randint(1,3))
  newImage()

try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

