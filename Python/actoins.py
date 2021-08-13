import subprocess
import os
import keyboard

__all__ = ["run_app",
           "open_folder",
           "vol_up",
           "vol_down",
           "vol_mute",
           ]


def run_app(path):
    '''
    Launch an app

    Params:
        path - an absolute path to .exe file
    '''
    if(not os.path.exists(path)):
        raise FileNotFoundError('The path does not exists')
    if(os.access(path, os.X_OK)):
        subprocess.Popen(path)
    else:
        raise Exception('The path is not an executable file')


def open_folder(path):
    '''
    Launch the explorer at the given folder

    Params:
        path - an absolute path to a folder
    '''
    if(os.path.isdir(path)):
        subprocess.Popen(f'explorer.exe {path}')
    else:
        raise Exception('The path given is not a directory')


def vol_up():
    '''
    Sets the main audio output 2 points up
    '''
    keyboard.send('volume_up')


def vol_down():
    '''
    Sets the main audio output 2 points down
    '''
    keyboard.send('volume_down')


def vol_mute():
    '''
    Mute / Unmute main audio
    '''
    keyboard.send('volume_mute')
