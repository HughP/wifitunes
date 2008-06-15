#!/usr/bin/env python

# Usage: ./setup.py py2app

from distutils.core import setup
import py2app

infoPlist = dict(
    CFBundleName='wifiTunes',
    CFBundleIconFile='wifiTunes',
    CFBundleIdentifier='groovework.wifiTunes',
    CFBundleGetInfoString='wifiTunes control panel',
    CFBundleVersion='0.9',
    CFBundleShortVersionString = '0.9',
    NSPrefPaneIconLabel='wifiTunes',
    NSPrefPaneIconFile='wifiTunes.icns',
    NSPrincipalClass='wifiTunesPref',
    NSMainNibFile='wifiTunesPref',
)

setup(
    name = "wifiTunes",
    plugin = ["wifiTunes.py"],
    data_files=["src", "img", "English.lproj", "wifiTunes.icns", "about.rtfd"],
    options=dict(py2app=dict(
        extension=".prefPane",
        plist=infoPlist,
    )),
)