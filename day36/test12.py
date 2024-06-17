import keyboard

def macro():
    keyboard.press('q')
    keyboard.press('w')
    keyboard.press('e')
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release('e')
    keyboard.release('w')
    keyboard.release('q')
    print("executing")

keyboard.add_hotkey('Z', macro)
keyboard.wait('esc')