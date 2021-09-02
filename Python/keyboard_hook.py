import json
import os
import keyboard
from time import sleep
from sys import exit

from actions import *
import actions as actions
from dummy_config import dummy_config


def config_to_func(action, args):
    if action == '':
        return lambda: placeholder()
    elif args == '':
        return lambda: getattr(actions, action)()
    else:
        return lambda: getattr(actions, action)(args)


def update_key_binding(key, function):
    pass


def check_config():
    '''
    Check if there is a config file in the same directory.
    if it can't file a config it will create a new one.
    '''
    if not os.path.exists('config.json'):
        with open('config.json', 'w') as conf:
            json.dump(dummy_config, conf)


def load_config():
    '''
    Reads the config file - currently set to the same directory!

    Returns:
        dict - contains all the config settings
    '''
    try:
        with open('config.json', 'r') as conf:
            config = json.load(conf)
            return config
    except FileNotFoundError:
        print("No config file was found")


def set_current_config(config):
    '''
    Sets all the actions from the loaded config file
    '''
    for key, value in config.items():
        action = config_to_func(value['action'], value['args'])
        keyboard.add_hotkey(key, action)

    # Adding akey combo for quiting the script
    keyboard.add_hotkey('F13+F21', exit)


if __name__ == "__main__":
    check_config()
    config = load_config()
    set_current_config(config)

    while True:
        sleep(1)
