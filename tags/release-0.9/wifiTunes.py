#    wifiTunes is a web based remote interface to your favorite music app
#    Copyright (C) 2008  Urs Kofmel
#
#    This file is part of wifiTunes.
#
#    wifiTunes is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    wifiTunes is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with wifiTunes.  If not, see <http://www.gnu.org/licenses/>.

import objc
from AppKit import *
from Foundation import *
from PreferencePanes import *
from PyObjCTools import NibClassBuilder, AppHelper
import os
import socket

# Uncomment this during development, you'll get exception tracebacks when
# the Python code fails.
#objc.setVerbose(1)

# set to True to have output of what is happening
Debug = False

# Location of the launchd plist
LaunchdPlist="~/Library/LaunchAgents/groovework.wifiTunes.plist"

class PortFormatter(NSFormatter):
    def stringForObjectValue_(self, object):
        if isinstance(object, (str, unicode)):
            return object
        return str(object)

    def getObjectValue_forString_errorDescription_(self, string):
        if Debug: print self, string
        if not string:
            if Debug: print "no data"
            return True, None, None
        if Debug: print "we have data"
        try:
            number = int(string)
        except:
            number = 0
        if Debug: print "number", number
        if number != 0:
            return True, NSString.stringWithString_(string), None
        return False, None, NSString.stringWithString_("ilegal character")

    def isPartialStringValid_newEditingString_errorDescription_(self, partialString, whatever):
        if Debug: print self, partialString, whatever
        try:
            number = int(partialString)
            newString = partialString
        except:
            number = 0
            newString = ""
        if number > 0 and number < 65536:
            return True, newString, None
        return False, newString, None

class wifiTunesPref(NSPreferencePane):
    # Interface Builder outlets
    startStopButton = objc.IBOutlet()
    portNumber = objc.IBOutlet()
    onLogin = objc.IBOutlet()
    statusText = objc.IBOutlet()
    sideImage = objc.IBOutlet()
    urlText = objc.IBOutlet()
    reachableText = objc.IBOutlet()
    aboutText = objc.IBOutlet()

    def initWithBundle_(self, bundle):
        # the bundle is loaded and some initialisation can be done
        if Debug: print "pre init"
        self = super(wifiTunesPref, self).initWithBundle_(bundle)
        if self is None: return None
        if Debug: print "post init"
        self.loadOnLogin = 0
        self.launch = None
        self.arguments = NSMutableArray.arrayWithCapacity_(2)
        self.defaultPort = "5555"
        self.lastUsedPort = ""
        self.running = False
        self.changed = False
        self.imageOn = NSImage.alloc().initWithContentsOfFile_(os.path.expanduser("~/Library/PreferencePanes/wifiTunes.prefPane/Contents/Resources/img/wifiTunesOn.tiff"))
        self.imageOff = NSImage.alloc().initWithContentsOfFile_(os.path.expanduser("~/Library/PreferencePanes/wifiTunes.prefPane/Contents/Resources/img/wifiTunesOff.tiff"))
        self.aboutTextFile = NSString.stringWithString_(os.path.expanduser("~/Library/PreferencePanes/wifiTunes.prefPane/Contents/Resources/about.rtfd"))
        self.hostname = ""
        self.ipv4 = ""
        self.getAddress()
        return self

    def mainViewDidLoad(self):
        # the main view is loaded and ready to display. Time to manipulate it's elements
        self.formatter = PortFormatter.alloc().init()
        self.portNumber.setFormatter_(self.formatter)
        self.portNumber.setStringValue_(self.defaultPort)
        self.sideImage.setImage_(self.imageOff)
        self.aboutText.readRTFDFromFile_(self.aboutTextFile)
        if Debug: print "mainViewDidLoad finished"

    def willSelect(self):
        # preference pane was selected. Load or create the plist.
        self.launch = NSMutableDictionary.dictionaryWithContentsOfFile_(os.path.expanduser(LaunchdPlist))
        if self.launch is None:
            # create an empty plist in memory
            self.launch = NSMutableDictionary.dictionary()
            # create default entrys for plist
            self.launch.setValue_forKey_(NSString.stringWithString_("groovework.wifiTunes"), "Label")
            self.arguments.insertObject_atIndex_(NSString.stringWithString_("~/Library/PreferencePanes/wifiTunes.prefPane/Contents/Resources/src/pyituneswebremote.py"), 0)
            self.arguments.insertObject_atIndex_(NSString.stringWithString_(self.defaultPort), 1)
            self.launch.setValue_forKey_(self.arguments, "ProgramArguments")
            self.launch.setValue_forKey_(True, "RunAtLoad")
            self.launch.setValue_forKey_(True, "Disabled")
        if Debug: print self.launch
        # set ProgramArguments[0] to correct (user) path
        self.arguments = self.launch.valueForKey_("ProgramArguments")
        path = self.arguments.objectAtIndex_(0)
        newpath = NSString.stringWithString_(os.path.expanduser(path))
        self.arguments.replaceObjectAtIndex_withObject_(0, newpath)
        # write to disk
        self.savePlist()
        # get current status
        self.getStatus()
        # set port number to last used
        self.lastUsedPort = self.arguments.objectAtIndex_(1)
        self.portNumber.setStringValue_(self.lastUsedPort)
        # set checkbox
        if self.launch.valueForKey_("Disabled") == False:
            self.onLogin.setState_(1)
        else:
            self.onLogin.setState_(0)

    def shouldUnselect(self):
        # write plist before leaving
        self.savePlist()
        return True

    @objc.IBAction
    def startStop_(self, sender):
        self.setPort()
        self.savePlist()
        if self.running == True:
            os.system("launchctl unload " + os.path.expanduser(LaunchdPlist))
        else:
            os.system("launchctl load -F " + os.path.expanduser(LaunchdPlist))
            self.getAddress()
        self.getStatus()
        if Debug: print "start / stop"
        #self.portNumber.stringValue_("")

    @objc.IBAction
    def toggleStartOnLogin_(self, sender):
        # check state of checkbox
        self.loadOnLogin = self.onLogin.state()
        # if checked
        if self.loadOnLogin == 0:
            if Debug: print "onLogin is off"
            # set launchd plist Disabled to true
            self.launch.setValue_forKey_(True, "Disabled")
        # else
        else:
            if Debug: print "onLogin is on"
            # set launchd plist Disabled to false
            self.launch.setValue_forKey_(False, "Disabled")
        # write launchd plist to disk
        self.savePlist()
        if Debug: print "onLogin was toggled"

    @objc.IBAction
    def portChanged_(self, sender):
        self.setPort()
        if Debug: print "port changed"

    @objc.IBAction
    def gotoDonate_(self, sender):
        os.system("open http://wifitunes.wordpress.com/donate/")

    @objc.IBAction
    def gotoURL_(self, sender):
        os.system("open http://wifitunes.wordpress.com/")

    def getAddress(self):
        self.hostname = socket.gethostname()
        if Debug: print self.hostname
        self.ipv4 = socket.gethostbyname(self.hostname)
        if Debug: print self.ipv4

    def getStatus(self):
        launchstatus = os.system("launchctl list | grep -q groovework.wifiTunes")
        if Debug: print launchstatus
        if launchstatus == 0:
            self.running = True
            self.statusText.setObjectValue_("wifiTunes is currently running.\nPress the Stop button to stop it.")
            self.startStopButton.setTitle_("Stop")
            self.sideImage.setImage_(self.imageOn)
            self.setLinkText("http://" + self.ipv4 + ":" + str(self.portNumber.stringValue()))
            self.enableReachableText("wifiTunes is now reachable at:")
        else:
            self.running = False
            self.statusText.setObjectValue_("wifiTunes is currently not running.\nPress the Start button to start it.")
            self.startStopButton.setTitle_("Start")
            self.sideImage.setImage_(self.imageOff)
            self.setLinkText("")
            self.enableReachableText("")
        if Debug: print "didSelect finished"

    def setPort(self):
        # if textfield is empty set to default port
        if self.portNumber.stringValue() == "":
            self.portNumber.setStringValue_(self.defaultPort)
        # write to arguments array
        newport = NSString.stringWithString_(self.portNumber.stringValue())
        self.arguments.replaceObjectAtIndex_withObject_(1, newport)
        if Debug: print self.arguments

    def savePlist(self):
        # reassemble the plist dictionary
        self.launch.setValue_forKey_(self.arguments, "ProgramArguments")
        # save the launchd plist
        plistPath = os.path.expanduser(LaunchdPlist)
        plistDir = os.path.dirname(plistPath)
        if os.path.isdir(plistDir) != True:
            try:
                os.mkdir(plistDir)
            except:
                print plistDir + " was not found, and can not be created"
                return False
        if os.access(plistDir, os.W_OK) == False:
            print "coud not write to " + plistDir + ". check permissions"
            return False
        if self.launch.writeToFile_atomically_(plistPath, True) == False:
            print "error writing plist"
            return False
        if Debug: print self.launch
        if Debug: print "plist written"
        return True

    def setLinkText(self, string):
        if string == "":
            self.urlText.setEnabled_(False)
            self.urlText.setSelectable_(False)
        else:
            self.urlText.setEnabled_(True)
            self.urlText.setSelectable_(True)
        attributString = NSMutableAttributedString.alloc().initWithString_(string)
        attributDict = NSMutableDictionary.dictionaryWithCapacity_(1)
        attributDict.setObject_forKey_(string, NSLinkAttributeName)
        attributDict.setObject_forKey_(NSFont.fontWithName_size_("Lucida Grande", 11), NSFontAttributeName)
        attributDict.setObject_forKey_(1, NSUnderlineStyleAttributeName)
        attributDict.setObject_forKey_(NSColor.colorWithDeviceRed_green_blue_alpha_(0.086, 0, 1, 1), NSForegroundColorAttributeName)
        attributRange = NSMakeRange(0, attributString.length())
        attributString.addAttributes_range_(attributDict.copy(), attributRange)
        self.urlText.setAttributedStringValue_(attributString)

    def enableReachableText(self, string):
        if string == "":
            self.reachableText.setEnabled_(False)
        else:
            self.reachableText.setEnabled_(True)
        attributString = NSMutableAttributedString.alloc().initWithString_(string)
        attributDict = NSMutableDictionary.dictionaryWithCapacity_(1)
        attributDict.setObject_forKey_(NSFont.fontWithName_size_("Lucida Grande", 11), NSFontAttributeName)
        attributRange = NSMakeRange(0, attributString.length())
        attributString.addAttributes_range_(attributDict.copy(), attributRange)
        self.reachableText.setAttributedStringValue_(attributString)

objc.removeAutoreleasePool()
