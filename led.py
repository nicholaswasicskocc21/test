import time
import RPi.GPIO as IO

IO.setmode(IO.BOARD)
IO.setwarnings(false)
IO.setup(IO.OUT)

while True:
  IO.output(40, IO.HIGH)
  time.sleep(5)
  
  IO.output(40, IO.LOW)
  time.sleep(5)
 
