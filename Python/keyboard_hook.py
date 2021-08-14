import json
import os
import keyboard
from time import sleep

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


if not os.path.exists('config.json'):
    with open('config.json', 'w') as conf:
        json.dump(dummy_config, conf)

with open('config.json', 'r') as conf:
    config = json.load(conf)

    for key, value in config.items():
        action = config_to_func(value['action'], value['args'])
        keyboard.add_hotkey(key, action)


# Sleeping to keep script alive
while True:
    sleep(1)
