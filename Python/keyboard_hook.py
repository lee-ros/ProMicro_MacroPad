import keyboard
from time import sleep

from actoins import run_app, open_folder
#import actions

# key:function mapping
key_functions = {
    'F13': lambda: print('F13 is pressed'),
    'F14': lambda: print('F14 is pressed'),
    'F15': lambda: print('F15 is pressed'),
    'F16': lambda: print('F16 is pressed'),
    'F17': lambda: print('F17 is pressed'),
    'F18': lambda: print('F18 is pressed'),
    'F19': lambda: print('F19 is pressed'),
    'F20': lambda: print('F20 is pressed'),
    'F21': lambda: print('F21 is pressed'),
}


# Define key bindings
for key, value in key_functions.items():
    keyboard.add_hotkey(key, value)


# Sleeping to keep script alive
while True:
    sleep(1)
