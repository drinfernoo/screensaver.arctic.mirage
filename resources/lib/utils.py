# -*- coding: utf-8 -*-
import xbmc
import xbmcaddon

_addon = xbmcaddon.Addon()
_id = _addon.getAddonInfo('id')

def log(msg, level=xbmc.LOGDEBUG):
    message = '{}: {}'.format(_id, msg)
    xbmc.log(msg=message, level=level)


def get_setting_string(setting):
    try:
        return _addon.getSettingString(setting)
    except:
        return '{}'.format(_addon.getSetting(setting))


def set_setting_string(setting, value):
    try:
        return _addon.setSettingString(setting, value)
    except:
        return _addon.setSetting(setting, value)
