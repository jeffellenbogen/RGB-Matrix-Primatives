# Used in main loop
from time import sleep
import random

###################################
# Graphics imports, constants and structures
###################################
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw

import paho.mqtt.client as mqtt

def on_message(client,userdata,message):
  global knobRvalue
  global knobGvalue 
  global knobBvalue
  global colorChanged

  
  print("Color Data Received " + message.topic + " " + message.payload)
  if (message.topic == "color/red"):
    knobRvalue = int(message.payload)
  elif (message.topic == "color/green"):
    knobGvalue = int(message.payload)
  elif (message.topic == "color/blue"):
    knobBvalue = int(message.payload)
  else: 
    print ("unknown topic")

  colorChanged = True

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

##subscribe to MQTT topic here to get changes to p5.js knobMaker page
knobRvalue = 0
knobGvalue = 0
knobBvalue = 0

donutSize = random.randint(10,60)
xCenterPt = random.randint(0,total_columns)
yCenterPt = random.randint(0,total_rows)

pause = .5
cycleCount = 0

image = Image.new("RGB", (total_columns,total_rows))
drawRect = ImageDraw.Draw(image)
drawCircle = ImageDraw.Draw(image)
drawPoint = ImageDraw.Draw(image)


drawRect.rectangle((0,0,total_columns,total_rows), fill = black)
matrix.SetImage(image,0,0)

#MQTT client setup
broker_address = "makerlabpi1"
client_name = "DonutMQTT"
client = mqtt.Client(client_name)
try:
  client.connect(broker_address)
except:
  print "Unable to connect to MQTT broker"
  exit(0)
client.loop_start() #starts looking for callbacks
client.on_message=on_message #sets callback to on_message function when message is received

#MQTT subscribe
subscribe_str = "color/#"
print("subscribing to " + subscribe_str)
client.subscribe(subscribe_str)
#client.publish("register/request", client_name) #not using this publish statement (topic, payload)

colorChanged = False

while True:
  donutSize = random.randint(10,30)
  xCenterPt = random.randint(-donutSize/2,total_columns+donutSize/2)
  yCenterPt = random.randint(-donutSize/2,total_rows+donutSize/2)

  #randomColor = random.randint(0,360)
  #donut_color ="hsl({}, 100%, 50%)".format(randomColor) 
  #donut_color = (255 - knobRvalue, 255 - knobGvalue, 255 - knobBvalue)
  #backgrdColor = (knobRvalue, knobGvalue, knobBvalue)

  ##commented off the inner blue part of each donut
  #drawPoint.point((xCenterPt,yCenterPt), fill = blue)
  '''for i in range (donutSize/2):
    drawCircle.ellipse((xCenterPt - i, yCenterPt - i, xCenterPt + i, yCenterPt + i), outline = blue )'''


  for i in range (donutSize/2,donutSize):
    donut_color = (255 - knobRvalue, 255 - knobGvalue, 255 - knobBvalue)
    backgrdColor = (knobRvalue, knobGvalue, knobBvalue)
    if colorChanged:
      drawRect.rectangle((0,0,total_columns,total_rows), fill = backgrdColor)
      colorChanged = False
    drawCircle.ellipse((xCenterPt - i, yCenterPt - i, xCenterPt + i, yCenterPt + i), outline = donut_color )
  
  matrix.SetImage(image, 0, 0)

  cycleCount+=1
  sleep(pause)
  if cycleCount > 10:
    cycleCount = 0
    drawRect.rectangle((0,0,total_columns,total_rows), fill = backgrdColor)
    matrix.SetImage(image,0,0)



