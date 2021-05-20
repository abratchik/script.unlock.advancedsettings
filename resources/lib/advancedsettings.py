# coding=utf-8
# Module: lockpicks
# Author: Alex Bratchik
# Created on: 20.05.2021
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import os
import xml.dom.minidom as xmldom

import xbmcvfs
import xbmcaddon

class AdvancedSettings():
    def __init__(self):
        self.id = "script.unlock.advancedsettings"
        self.addon = xbmcaddon.Addon(self.id)
        self.kodi_settings_path = os.path.join(os.path.join(xbmcvfs.translatePath("special://xbmc"),
                                                            "system"),
                                               "settings")

        self.settings_ui_file = os.path.join(self.kodi_settings_path, "settings.xml")

    def unlock(self):
        self.addon.openSettings(self.id)

        if self.addon.getSettingBool("unlock"):
            self.unlock()
        else:
            self._lock()

    def _unlock(self):
        settings_ui_doc = xmldom.parse(self.settings_ui_file)

        pass

    def _lock(self):
        pass