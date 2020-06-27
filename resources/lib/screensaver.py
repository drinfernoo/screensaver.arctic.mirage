# -*- coding: utf-8 -*-
import xbmc
import xbmcgui

from resources.lib import utils


class Screensaver(xbmcgui.WindowXMLDialog):
    
    class ExitMonitor(xbmc.Monitor):
        
        def __init__(self, exit_callback):
            self.exit_callback = exit_callback
            
        def onScreensaverActivated(self):
            utils.log('Screensaver Activated')
            
        def onScreensaverDeactivated(self):
            utils.log('Screensaver Deactivated')
            
            try:
                self.exit_callback()
            except AttributeError:
                utils.log('Callback method not yet available.')
    
    
    def __init__(self, *args, **kwargs):
        self.exit_monitor = self.ExitMonitor(self.exit)
        self.path = utils.get_setting_string('screensaver.arctic.mirage.path')
        utils.log(self.path)
    
    def onInit(self):
        self.character = self.getControl(1298)
        
        if self.path and self.exit_monitor:
            self.setProperty('screensaver.arctic.mirage.path', self.path)

    def exit(self):
        if self.exit_monitor:
            del self.exit_monitor
            
        self.close()
