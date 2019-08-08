
# Used in main loop
from time import sleep
import random
import time

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

start = time.time()
elapsed_time = 0
last_reset = 0

matrix = RGBMatrix(options = options)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white = (250,250,250)
white_fade = (75,75,75)
black = (0,0,0)


spinSpeed = .05

sectors = 12
flowersize = 120
numFlowerRows = 1
numFlowerColumns = 1

sectorAngle = 360 / sectors
spacingFlowerRows = (total_columns - (flowersize * numFlowerColumns))/ (numFlowerColumns + 1)
spacingFlowerColumns = (total_rows - (flowersize * numFlowerRows)) / (numFlowerRows + 1)



###################################
# Main loop 
###################################
image = Image.new("RGB", (total_columns,total_rows))
#flower = Image.new("RGB", (flowersize, flowersize)
draw = ImageDraw.Draw(image)


while True:
  if (elapsed_time > 5):
    sectors = random.randint(3,12)
    flowersize = random.randint(10,60)
    numFlowerRows = random.randint(1,6)
    numFlowerColumns = random.randint(1,4)

    sectorAngle = 360 / sectors
    spacingFlowerRows = (total_columns - (flowersize * numFlowerColumns))/ (numFlowerColumns + 1)
    spacingFlowerColumns = (total_rows - (flowersize * numFlowerRows)) / (numFlowerRows + 1)

    elapsed_time=0
    last_reset=time.time()
    #draw.rectangle((0,0,total_columns,total_rows), fill=black)
    #matrix.SetImage(image,0,0)
  elapsed_time = time.time()-last_reset  

  randomColor = random.randint(0,360) 
  fill_color = "hsl({}, 30%, 50%)".format(randomColor) 
  fade_color = "hsl({}, 30%, 20%)".format(randomColor) 
  for k in range (sectors):
    for i in range(numFlowerColumns):
      for j in range(numFlowerRows):
        #draw.pieslice((i*spacingFlowerColumns,j*spacingFlowerRows, i*spacingFlowerColumns + flowersize, j*spacingFlowerRows + flowersize),sectorAngle * k, sectorAngle * (k+1),outline = blue, fill = red)       
        x1=(i+1)*spacingFlowerRows + i*flowersize
        y1=(j+1)*spacingFlowerColumns + j*flowersize
        x2=(i+1)*spacingFlowerRows + i*flowersize + flowersize
        y2=(j+1)*spacingFlowerColumns + j*flowersize + flowersize
        draw.pieslice((x1,y1,x2,y2),sectorAngle * k, sectorAngle * (k+1),outline = white, fill = fill_color)
    matrix.SetImage(image, 0, 0)
    sleep(spinSpeed)
    for i in range(numFlowerColumns):
      for j in range(numFlowerRows):
        x1=(i+1)*spacingFlowerRows + i*flowersize
        y1=(j+1)*spacingFlowerColumns + j*flowersize
        x2=(i+1)*spacingFlowerRows + i*flowersize + flowersize
        y2=(j+1)*spacingFlowerColumns + j*flowersize + flowersize
        draw.pieslice((x1,y1,x2,y2),sectorAngle * (k-1), sectorAngle * k,outline = white_fade, fill =  fade_color)
    matrix.SetImage(image, 0, 0)

    ###This sections adds a blackout of the faded sector
    '''sleep(spinSpeed)
    for i in range(numFlowerColumns):
      for j in range(numFlowerRows):
        x1=(i+1)*spacingFlowerRows + i*flowersize
        y1=(j+1)*spacingFlowerColumns + j*flowersize
        x2=(i+1)*spacingFlowerRows + i*flowersize + flowersize
        y2=(j+1)*spacingFlowerColumns + j*flowersize + flowersize
        draw.pieslice((x1,y1,x2,y2),sectorAngle * (k-2), sectorAngle * (k-1), fill =  black)
    matrix.SetImage(image, 0, 0)'''


try:
  print("Press CTRL-C to stop")
  while True:
    sleep(100)
except KeyboardInterrupt:
  exit(0)

