# coding=utf-8
# Module: main
# Author: Alex Bratchik
# Created on: 20.05.2021
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
"""
Unlock Kodi Advanced Settings
"""
from resources.lib.advancedsettings import AdvancedSettings

if __name__ == '__main__':
    AdvancedSettings = AdvancedSettings()

    AdvancedSettings.unlock()
