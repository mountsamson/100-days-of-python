import keyboard
import time

#code 

keys_pressed = []


# Define the functions
def cold_snap():
    keys = ['q', 'q', 'q', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01) 
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01) 
    print('Cold Snap')

def ghost_walk():
   keys = ['q', 'q', 'w', 'r']
   for key in keys:
        keyboard.press(key)
        time.sleep(0.01) 
   for key in keys:
        keyboard.release(key)
        time.sleep(0.01) 
   print('Ghost Walk')

def ice_wall():
    keys = ['q', 'q', 'e', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01) 
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01) 
    print('Ice Wall')
    

def emp():
    keys = ['w', 'w', 'w', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01) 
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01) 
    print('EMP')
    

def tornado():
    keys = ['w', 'w', 'q', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01) 
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01) 
    print('Tornado')

def alacrity():
    keys = ['w', 'w', 'e', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01)
    print('Alacrity')

def sun_strike():
    keys = ['e', 'e', 'e', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01)
    print('Sun Strike')

def forge_spirit():
    keys = ['e', 'e', 'q', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01)
    print('Forge Spirit')

def chaos_meteor():
    keys = ['e', 'e', 'w', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01)
    print('Chaos Meteor')

def deafening_blast():
    keys = ['q', 'w', 'e', 'r']
    for key in keys:
        keyboard.press(key)
        time.sleep(0.01)
    for key in keys:
        keyboard.release(key)
        time.sleep(0.01)
    print('Deafening Blast')

# Bind the keys to the functions
keyboard.add_hotkey('1', cold_snap)
keyboard.add_hotkey('2', ghost_walk)
keyboard.add_hotkey('3', ice_wall)
keyboard.add_hotkey('4', emp)
keyboard.add_hotkey('5', tornado)
keyboard.add_hotkey('6', alacrity)
keyboard.add_hotkey('7', sun_strike)
keyboard.add_hotkey('8', forge_spirit)
keyboard.add_hotkey('9', chaos_meteor)
keyboard.add_hotkey('z', deafening_blast)

# Block forever
keyboard.wait()