#!/bin/bash

BuildDir="diskimage"
ResourceDir="dmgfiles"
TempImage="Temp.dmg"
ImageName="wifiTunes"

if test -d dist/wifiTunes.prefPane ; then
    echo ".prefPane exists"
else
    echo "no .prefPane found"
    exit 1
fi

mkdir "$BuildDir"
mv dist/wifiTunes.prefPane "$BuildDir"
cp "$ResourceDir/background.png" "$BuildDir/background.png"
SetFile -a V "$BuildDir/background.png"
hdiutil create "$TempImage" -srcfolder "$BuildDir" -fs HFS+ -volname "$ImageName" -format UDRW -ov
hdiutil attach "$TempImage" -mount required -mountroot ./

cp "$ResourceDir/dmg_DS_Store" "$ImageName/.DS_Store"
SetFile -a V "$ImageName/.DS_Store"

hdiutil detach "./$ImageName"
if test -f "$ImageName.dmg" ; then
    rm "$ImageName.dmg"
fi
hdiutil convert "$TempImage" -format UDBZ -o "$ImageName.dmg"

rm -rf "$BuildDir"
rm "$TempImage"
