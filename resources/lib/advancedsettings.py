# coding=utf-8
# Module: lockpicks
# Author: Alex Bratchik
# Created on: 20.05.2021
# License: GPL v.3 https://www.gnu.org/copyleft/gpl.html
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

import xbmc
import xbmcvfs
import xbmcaddon

ADSFNAME = "advancedsettings.xml"
GUIFNAME = "guisettings.xml"
PLGFNAME = "settings.xml"


class AdvancedSettings():
    def __init__(self):
        self.id = "script.unlock.advancedsettings"
        self.addon = xbmcaddon.Addon(self.id)
        self.path = self.addon.getAddonInfo('path')
        self.ads_path = xbmcvfs.translatePath("special://userdata")
        self.data_path = xbmcvfs.translatePath(self.addon.getAddonInfo('profile'))

        self.ads_file = os.path.join(self.ads_path, ADSFNAME)
        self.gui_file = os.path.join(self.ads_path, GUIFNAME)
        self.plg_file = os.path.join(os.path.join(self.path, "resources"), PLGFNAME)

        self.adv_settings = self.load_xml_from_file(self.ads_file)
        self.gui_settings = self.load_xml_from_file(self.gui_file)
        self.plg_settings = self.load_xml_from_file(self.plg_file)

    def edit(self):

        self._load()
        self.addon.openSettings(self.id)
        self._save()

    def _load(self):

        for cat in self.plg_settings.findall("category"):
            for s in cat.findall("setting[@id]"):
                setting_id = s.attrib['id']
                self.addon.setSetting(setting_id, self._get_adv_setting_value(cat, s))

    def _save(self):
        if self.adv_settings is None:
            self.adv_settings = ET.fromstring("<advancedsettings version='1.0' />")

        for cat in self.plg_settings.findall("category"):
            for s in cat.findall("setting[@id]"):
                setting_id = s.attrib['id']
                value = self.addon.getSetting(setting_id)

                self._save_adv_setting_value(cat, s, value)

            # remove empty categories
            adv_cat = self.adv_settings.find(cat.attrib['id'])
            if not (adv_cat is None) and len(adv_cat) == 0:
                self.adv_settings.remove(adv_cat)

        self.save_pretty_xml(self.adv_settings, self.ads_file)

    def _save_adv_setting_value(self, cat, s, value):
        xbmc.log("Category %s, setting %s" % (cat.attrib['id'], s.attrib['id']), xbmc.LOGDEBUG)
        default = s.attrib['default'] if 'default' in s.attrib else ""

        section_tag = cat.attrib['id']
        section = self.adv_settings if self._is_root_cat(cat) else self.adv_settings.find(section_tag)
        if section is None:
            section = ET.SubElement(self.adv_settings, section_tag)

        setting_tag = s.attrib['id'].partition("#")[0]
        setting = section.find(setting_tag)

        if default == value:
            if not (setting is None):
                section.remove(setting)
            return

        if setting is None:
            setting = ET.SubElement(section, setting_tag)

        self._write_setting_value(setting, s,
                                  self._reverse_lookup_enum(value, s) if s.attrib['type'] == "enum" else value)

    def _get_adv_setting_value(self, cat, s):
        xbmc.log("Category %s, setting %s" % (cat.attrib['id'], s.attrib['id']), xbmc.LOGDEBUG)
        if self.adv_settings is None:
            xbmc.log("%s not found" % ADSFNAME, xbmc.LOGDEBUG)
            return self._get_gui_setting_value(cat, s)

        section_tag = cat.attrib['id']
        section = self.adv_settings if self._is_root_cat(cat) else self.adv_settings.find(section_tag)
        if section is None:
            xbmc.log("Section %s not found" % section_tag, xbmc.LOGDEBUG)
            return self._get_gui_setting_value(cat, s)

        setting = section.find(s.attrib['id'].partition("#")[0])
        if not (setting is None):
            value = self._read_setting_value(setting, s)
            if s.attrib['type'] == "enum":
                return self._lookup_enum(value, s)
            else:
                return value
        else:
            xbmc.log("Setting %s not found" % s.attrib['id'], xbmc.LOGDEBUG)
            return self._get_gui_setting_value(cat, s)

    def _get_gui_setting_value(self, cat, s):
        setting_id = "%s.%s" % (cat.attrib['id'], s.attrib['id'])
        default = s.attrib['default'] if 'default' in s.attrib else ""
        setting = self.gui_settings.find(".//setting[@id='%s']" % setting_id)
        if not (setting is None):
            return setting.text
        else:
            return default

    @staticmethod
    def _is_root_cat(cat):
        return 'root' in cat.attrib and cat.attrib['root'] == "true"

    @staticmethod
    def _lookup_enum(value, s):
        enummap = s.find("enummap[@value='%s']" % value)
        if enummap is None:
            return value
        else:
            return enummap.attrib['key']

    @staticmethod
    def _reverse_lookup_enum(key, s):
        enummap = s.find("enummap[@key='%s']" % key)
        if enummap is None:
            return key
        else:
            return enummap.attrib['value']

    @staticmethod
    def _read_setting_value(setting, s):
        if "#" in s.attrib['id']:
            idc = s.attrib['id'].split("#")
            xbmc.log("Setting attribute %s of setting  %s" % (idc[1], s.attrib['id']))
            if idc[1] in setting.attrib:
                return setting.attrib[idc[1]]
            else:
                return s.attrib['default'] if 'default' in s.attrib else ""
        else:
            return setting.text

    @staticmethod
    def _write_setting_value(setting, s, value):
        if "#" in s.attrib['id']:
            idc = s.attrib['id'].split("#")
            xbmc.log("Setting attribute %s of setting  %s" % (idc[1], s.attrib['id']))
            setting.set(idc[1], value)
        else:
            setting.text = value

    @staticmethod
    def _set_child_text(element, child_tag, value):
        child = element.find(child_tag)
        if not (child is None):
            child.text = value

    @staticmethod
    def load_xml_from_file(filename):
        try:
            tree = ET.parse(filename)
            return tree.getroot()
        except:
            return None

    @staticmethod
    def save_pretty_xml(element, output_xml):
        xml_string = minidom.parseString(ET.tostring(element)).toprettyxml()
        xml_string = os.linesep.join(
            [s for s in xml_string.splitlines() if s.strip()])
        with open(output_xml, "w") as file_out:
            file_out.write(xml_string)
