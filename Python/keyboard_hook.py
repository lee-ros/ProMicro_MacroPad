import keyboard
from time import sleep

from actoins import run_app
#import actions

# Define key bindings
keyboard.add_hotkey('F13', run_app, args=[
                    r"C:\Program Files\PuTTY\putty.exe"])
keyboard.add_hotkey('F14', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F15', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F16', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F17', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F18', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F19', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F20', lambda: print('F14 Pressed'))
keyboard.add_hotkey('F21', lambda: print('F14 Pressed'))

# Sleeping to keep script alive
while True:
    sleep(1)
