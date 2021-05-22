# coding=utf-8
# Module: lockpicks
# Author: Alex Bratchik
# Created on: 20.05.2021
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import os
import xml.etree.ElementTree as ET

import xbmcvfs
import xbmcaddon

SETTINS = "settings.xml"

class AdvancedSettings():
    def __init__(self):
        self.id = "script.unlock.advancedsettings"
        self.addon = xbmcaddon.Addon(self.id)
        self.kodi_settings_path = os.path.join(os.path.join(xbmcvfs.translatePath("special://xbmc"),
                                                            "system"),
                                               "settings")
        self.data_path = xbmcvfs.translatePath(self.addon.getAddonInfo('profile'))

        self.settings_ui_file = os.path.join(self.kodi_settings_path, SETTINS)

    def unlock(self):
        self.addon.openSettings(self.id)

        # if self.addon.getSettingBool("unlock"):
        #     self.unlock()
        # else:
        #     self._lock()

    def _unlock(self):
        # tree = ET.parse(self.settings_ui_file)
        # root = tree.getroot()
        #
        # for cat in root.findall(".//category"):
        #     self._set_child_text(cat, "visible", "true")
        #     if cat.get("label"):
        #         for s in cat.findall(".//setting"):
        #             if s.get("label"):
        #                 lvl = s.find("level")
        #                 if not (lvl is None) and lvl.text == "4":
        #                     lvl.text = "3"

        pass

    def _lock(self):
        pass

    @staticmethod
    def _set_child_text(element, child_tag, value):
        child = element.find(child_tag)
        if not (child is None):
            child.text = value