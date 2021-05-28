# Unlock Kodi Advanced Settings

This addon allows to unlock the power of hidden Kodi system settings and
edit them through the System menu of Kodi. 

## Background
Kodi mediacenter is highly customizable system and has tons of settings,
which can be only changed by creating [advancedsewttings.xml](https://kodi.wiki/view/Advancedsettings.xml) file in the 
**userdata** folder. Changing these parameters requires manual authoring of 
the XML, which is error-prone and not always convenient.

This plugin enables editing of **advancedsettings.xml** similar to editing
settings of any other plugin.

## Installation 
1. Download  [this file](https://abratchik.github.io/kodi.repository/matrix/repository.abratchik/repository.abratchik-1.0.2.zip)
2. Navigate to **System/Add-ons/Install from the zip file** and 
   specify the file downloaded on the previous step. 
3. Navigate to **System/Add-ons/Alex Bratchik Kodi repository/
   Program add-ons**, click on "Unlock Kodi Advanced Settings" and 
   install it.
   
## User manual
Editing **advancedsettings.xml** is simple - just run the plugin. If you 
already have advancedsettings.xml defined in your system, it will be loaded
accordingly.

Once you complete editing changes and save them, advancedsettings.xml will be
updated (or created if it was not present in your system) in the **userddata**
folder. Old advancedsettings.xml file will be stored with **.bak** extension
in the userdata folder. 

If a setting is reverted to its default value, it will not be written to the 
advancedsettings.xml file. Parent tags without non-default settings will be automatically
removed from the file.

## Known limitations
1. Any formatting or manual comments in advancedsettings.xml will not be 
   preserved. 
2. Some settings may be not supported. In this case it is still possible to set
   them manually by editing advancedsettings.xml file. Such settings will NOT
   be overwritten by the plugin.


## Disclaimer
This is a non-commercial community-supported addon.
This plugin was created just fo fun and has no relation to official 
Kodi software. PLease know what you are doing and use at your own risk. 
Author bears no liability for any changes made by this plugin in your 
system.

License: [GPL v.3](http://www.gnu.org/copyleft/gpl.html)