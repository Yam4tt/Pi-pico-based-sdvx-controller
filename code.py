#SDVX Controller firmware
#Made by: Jakub Harasti (Yam4tt)
import usb_hid
import digitalio
import board
import rotaryio
from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode


#"BT"
BT1_pin = board.GP6
BT2_pin = board.GP7 
BT3_pin = board.GP8
BT4_pin = board.GP9
#"FX"
FXR_pin = board.GP10
FXL_pin = board.GP11
#tlacidlo start
STRT_pin = board.GP13
#encoders
encoderL = rotaryio.IncrementalEncoder(board.GP26,board.GP27)
LastPositionL = 0
encoderR = rotaryio.IncrementalEncoder(board.GP4,board.GP3)
LastPositionR = 0

keyboard = Keyboard(usb_hid.devices)
mouse = Mouse(usb_hid.devices)



BT1 = digitalio.DigitalInOut(BT1_pin)
BT1.direction = digitalio.Direction.INPUT
BT1.pull =digitalio.Pull.DOWN

BT2 = digitalio.DigitalInOut(BT2_pin)
BT2.direction = digitalio.Direction.INPUT
BT2.pull =digitalio.Pull.DOWN

BT3 = digitalio.DigitalInOut(BT3_pin)
BT3.direction = digitalio.Direction.INPUT
BT3.pull =digitalio.Pull.DOWN

BT4 = digitalio.DigitalInOut(BT4_pin)
BT4.direction = digitalio.Direction.INPUT
BT4.pull =digitalio.Pull.DOWN

FXL = digitalio.DigitalInOut(FXL_pin)
FXL.direction = digitalio.Direction.INPUT
FXL.pull =digitalio.Pull.DOWN

FXR = digitalio.DigitalInOut(FXR_pin)
FXR.direction = digitalio.Direction.INPUT
FXR.pull =digitalio.Pull.DOWN

STRT = digitalio.DigitalInOut(STRT_pin)
STRT.direction = digitalio.Direction.INPUT
STRT.pull =digitalio.Pull.DOWN



while True:
    
    if BT1.value:
        #print("BT1")
        keyboard.press(Keycode.A)
    else:
        keyboard.release(Keycode.A)  
        #time.sleep(0.02)
    
    if BT2.value:
        #print("BT2")
        keyboard.press(Keycode.B)
    else:
        keyboard.release(Keycode.B)
       # time.sleep(0.02)
         
    if BT3.value:
        #print("BT3")
        keyboard.press(Keycode.C)
    else:
        keyboard.release(Keycode.C)     
       # time.sleep(0.02)
    
    if BT4.value:
        #print("BT4")
        keyboard.press(Keycode.D)
    else:
        keyboard.release(Keycode.D)
       # time.sleep(0.02)
        
    if FXL.value:
        #print("FXL")
        keyboard.press(Keycode.V)
    else:
        keyboard.release(Keycode.V)
        #time.sleep(0.02)
        
    if FXR.value:
        #print("FXR")
        keyboard.press(Keycode.M)
    else:
        keyboard.release(Keycode.M)
       # time.sleep(0.02)
        
    if STRT.value:
        #print("START")
        keyboard.press(Keycode.ENTER)
    else:
        keyboard.release(Keycode.ENTER)
        

    positionL = encoderL.position
    positionL_change = positionL - LastPositionL   
    if LastPositionL is None or LastPositionL != positionL:
          print(positionL)
    if positionL_change > 0:
           for _ in range(positionL_change):
               mouse.move(y=-1)
               break
              
    elif positionL_change < 0:
           for _ in range(- positionL_change):
               mouse.move(y=1)
               break
     
    LastPositionL = positionL
     
    positionR = encoderR.position
    positionR_change = positionR - LastPositionR   
    if LastPositionR is None or LastPositionR != positionR:
          print(positionR)
    if positionR_change > 0:
           for _ in range(positionR_change):
               mouse.move(x=-1)
               break
    elif positionR_change < 0:
           for _ in range(- positionR_change):
               mouse.move(x=1)
               break
     
    LastPositionR = positionR
