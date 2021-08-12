import subprocess
import os


def run_app(path):
    '''
    this function is used to launch an app
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
    this function is used to launch the explorer at the given folder
    Params:
        path - an absolute path to a folder
    '''
    if(os.path.isdir(path)):
        subprocess.Popen(f'explorer.exe {path}')
    else:
        raise Exception('The path given is not a directory')
