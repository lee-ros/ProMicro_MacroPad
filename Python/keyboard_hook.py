import keyboard
from time import sleep

# Define key bindings
keyboard.add_hotkey('F13', lambda: print('F13 Pressed'))
keyboard.add_hotkey('F14', lambda: print('F14 Pressed'))

# Sleeping to keep script alive
while True:
    sleep(1)
