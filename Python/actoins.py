import subprocess
import os


def run_app(path):
    '''
    this function is used to launch an app
    Params:
        path - an absolute path to .exe file
    '''
    if(os.access(path, os.X_OK)):
        subprocess.Popen(path)
    else:
        if(os.path.exists(path)):
            raise Exception('The path is not an executable file')
        else:
            raise FileNotFoundError('The path is not an executable file')
