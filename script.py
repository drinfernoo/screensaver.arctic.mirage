# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon

import os
import sys

from resources.lib import utils

_addon = xbmcaddon.Addon()
_id = _addon.getAddonInfo('id')

def get_params():
    for arg in sys.argv:
        if arg == 'script.py':
            pass
        elif '=' in arg:
            arg_split = arg.split('=', 1)
            if arg_split[0] and arg_split[1]:
                return arg_split


def change_label():
    call = 'Skin.SetString({}.name)'.format(_id)
    return call

def choose_path():
    call = ('RunScript(script.skinshortcuts,'
            'type=widgets'
            '&showNone=False'
            '&skinWidgetName={0}.name'
            '&skinWidgetPath={0}.path)'.format(_id))
    return call


if __name__ == '__main__':
    params = get_params()
    
    if params[0] == 'mode':
        call = None
        
        if params[1] == 'label':
            call = change_label()
        elif params[1] == 'choose':
            call = choose_path()

        if call:
            xbmc.executebuiltin(call, wait=True)
